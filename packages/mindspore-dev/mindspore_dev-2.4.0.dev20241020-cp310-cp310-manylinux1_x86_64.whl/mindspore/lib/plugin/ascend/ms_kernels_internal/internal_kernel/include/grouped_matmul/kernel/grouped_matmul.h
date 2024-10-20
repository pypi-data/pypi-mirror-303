/**
 * Copyright (c) Huawei Technologies Co., Ltd. 2024. All rights reserved.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

#ifndef MS_KERNELS_INTERNAL_KERNEL_ASCENDC_GROUPED_MATMUL_H_
#define MS_KERNELS_INTERNAL_KERNEL_ASCENDC_GROUPED_MATMUL_H_

#include "grouped_matmul_utils.h"
#include "../tiling_data.h"

namespace GROUPED_MATMUL {

#define DTYPE_X half
#define DTYPE_WEIGHT half
#define DTYPE_BIAS half
#define DTYPE_Y half

/*@brief store variables for core split configuration
 */
struct MNConfig {
  uint32_t m;
  uint32_t k;
  uint32_t n;
  uint32_t baseM;
  uint32_t baseN;
  uint32_t mIdx;
  uint32_t nIdx;
  uint32_t blockDimM;
  uint32_t blockDimN;
  uint32_t singleM;
  uint32_t singleN;
  uint32_t ubBaseN;
  uint32_t ubCalSize;
};

/** @brief GroupMatmul operator Class
 */
template <typename ComputeType>
class GroupedMatmulProcess {
 private:
  __aicore__ inline void Process_();

  ComputeType &computeOp;  // inernal computation operator
  const GroupedMatmulTilingData *__restrict tilingData;

  uint32_t blockIdx;
  uint32_t subBlockIdx;
  uint32_t coreIdx;
  uint32_t groupNum;
  uint32_t coreNum;
  uint32_t baseM;
  uint32_t baseN;
  uint32_t ubBaseM;
  uint32_t ubBaseN;
  uint32_t ubCalSize;
  uint32_t ubRestBytes;

 public:
  /** @brief constructor */
  __aicore__ inline GroupedMatmulProcess(ComputeType &computeOp_) : computeOp(computeOp_) {}

  __aicore__ inline void Init(const GroupedMatmulTilingData *__restrict tiling);

  __aicore__ inline void Process();
};

template <typename ComputeType>
__aicore__ inline void GroupedMatmulProcess<ComputeType>::Init(const GroupedMatmulTilingData *__restrict tiling) {
  blockIdx = GetBlockIdx();
  subBlockIdx = GetSubBlockIdx();
  coreIdx = blockIdx / GetTaskRation();
  tilingData = tiling;
  groupNum = tilingData->groupedMatmulBaseParams.groupNum;
  baseM = tilingData->mmTilingData.baseM;
  baseN = tilingData->mmTilingData.baseN;
  ubBaseM = tilingData->groupedMatmulBaseParams.ubBaseM;
  ubBaseN = tilingData->groupedMatmulBaseParams.ubBaseN;
  coreNum = tilingData->groupedMatmulBaseParams.coreNum;
  ubCalSize = tilingData->groupedMatmulBaseParams.ubCalSize;
  ubRestBytes = tilingData->groupedMatmulBaseParams.ubRestBytes;
}

template <typename ComputeType>
__aicore__ inline void GroupedMatmulProcess<ComputeType>::Process() {
  auto &ubM = tilingData->groupedMatmulBaseParams.mList;
  auto &ubK = tilingData->groupedMatmulBaseParams.kList;
  auto &ubN = tilingData->groupedMatmulBaseParams.nList;

  MNConfig mnConfig;
  mnConfig.ubBaseN = ubBaseN;
  mnConfig.ubCalSize = ubCalSize;
  uint32_t count = 0;
  uint32_t wOutOffset = 0;  // for antiquant
  for (uint32_t groupIdx(0); groupIdx < groupNum; ++groupIdx) {
    mnConfig.m = ubM[groupIdx];
    mnConfig.k = ubK[groupIdx];
    mnConfig.n = ubN[groupIdx];
    uint32_t dimM = Ceil(mnConfig.m, baseM);
    uint32_t dimN = Ceil(mnConfig.n, baseN);
    mnConfig.singleM = baseM;
    mnConfig.singleN = baseN;
    mnConfig.blockDimM = dimM;
    mnConfig.blockDimN = dimN;

    uint32_t curCount = count + dimM * dimN;
    uint32_t curBlock = coreIdx >= count ? coreIdx : coreIdx + coreNum;
    while (curBlock < curCount) {
      mnConfig.mIdx = (curBlock - count) / dimN;
      mnConfig.nIdx = (curBlock - count) % dimN;
      if ASCEND_IS_AIC {
        computeOp.MMCompute(groupIdx, mnConfig, subBlockIdx, wOutOffset);
      }
      curBlock += coreNum;
    }
    wOutOffset += mnConfig.k * mnConfig.n;
    count = curCount % coreNum;
  }
}

/** @brief intenal computation class
 */
template <class mmType, bool sync = false>
class GroupedMatmulCompute {
 public:
  using AT = typename mmType::AT::T;
  using BT = typename mmType::BT::T;
  using CT = typename mmType::CT::T;
  using BiasT = typename mmType::BiasT::T;
  using WT = DTYPE_WEIGHT;

  /** @brief constructor */
  __aicore__ inline GroupedMatmulCompute(typename mmType::MT &mm_) : mm(mm_) {}

  __aicore__ inline void Init(GM_ADDR x, GM_ADDR weight, GM_ADDR bias, GM_ADDR scale, GM_ADDR offset,
                              GM_ADDR antiquantScale, GM_ADDR antiquantOffset, GM_ADDR y, GM_ADDR workspace,
                              const GroupedMatmulTilingData *__restrict tiling, TPipe *tPipe);

  __aicore__ inline void MMCompute(uint32_t groupIdx, MNConfig &mnConfig, uint32_t subBlockIdx, uint64_t wOutOffset);

  __aicore__ inline void MMSync(bool waitIterateAll, bool &mmWaitStatus, bool &firstMM);

  __aicore__ inline void CastWeightProcess(uint32_t curSingleN, uint64_t wInOffset, uint64_t wOutOffset,
                                           MNConfig &mnConfig);
  __aicore__ inline void CastWeightCompute(uint32_t curCalcK, uint32_t curCalcAlignN);
  __aicore__ inline void DataCopyScaleAndOffset(uint32_t curBaseN, uint32_t alignBaseN, uint64_t scaleOffset,
                                                uint32_t offsetN);

 private:
  TPipe *pipe;
  typename mmType::MT &mm;  // matmul operator
  bool hasBias = false;
  uint32_t mmDataTypeSize;
  GM_ADDR xTensorPtr;
  GM_ADDR weightTensorPtr;
  GM_ADDR biasTensorPtr;
  GM_ADDR yTensorPtr;
  GM_ADDR antiScaleTensorPtr;
  GM_ADDR antiOffsetTensorPtr;
  GlobalTensor<AT> xGm;
  GlobalTensor<BT> weightGm;
  GlobalTensor<BiasT> biasGm;
  GlobalTensor<CT> yGm;
};

template <typename mmType, bool sync>
__aicore__ inline void GroupedMatmulCompute<mmType, sync>::Init(GM_ADDR x, GM_ADDR weight, GM_ADDR bias, GM_ADDR scale,
                                                                GM_ADDR offset, GM_ADDR antiquantScale,
                                                                GM_ADDR antiquantOffset, GM_ADDR y, GM_ADDR workspace,
                                                                const GroupedMatmulTilingData *__restrict tiling,
                                                                TPipe *tPipe) {
  xTensorPtr = x;
  weightTensorPtr = weight;
  biasTensorPtr = bias;
  yTensorPtr = y;
  pipe = tPipe;
  if (bias != nullptr && GetTensorAddr<BiasT>(0, biasTensorPtr) != nullptr) {
    hasBias = true;
  }
}

template <typename mmType, bool sync>
__aicore__ inline void GroupedMatmulCompute<mmType, sync>::MMCompute(uint32_t groupIdx, MNConfig &mnConfig,
                                                                     uint32_t subBlockIdx, uint64_t wOutOffset) {
  if (subBlockIdx != 0) {
    return;
  }

  uint32_t curSingleN = mnConfig.singleN;
  uint32_t tailN = mnConfig.nIdx * mnConfig.singleN;
  if (mnConfig.nIdx == mnConfig.blockDimN - 1) {
    curSingleN = mnConfig.n - tailN;
  }
  uint32_t curSingleM = mnConfig.singleM;
  if (mnConfig.mIdx == mnConfig.blockDimM - 1) {
    curSingleM = mnConfig.m - mnConfig.mIdx * curSingleM;
  }
  uint64_t xOffset = mnConfig.mIdx * mnConfig.singleM * mnConfig.k;
  uint64_t wOffset = tailN;
  uint64_t outOffset = mnConfig.mIdx * mnConfig.singleM * mnConfig.n + tailN;
  // init global buffer
  xGm.SetGlobalBuffer(GetTensorAddr<AT>(groupIdx, xTensorPtr));
  weightGm.SetGlobalBuffer(GetTensorAddr<BT>(groupIdx, weightTensorPtr));
  yGm.SetGlobalBuffer(GetTensorAddr<CT>(groupIdx, yTensorPtr));
  mm.SetOrgShape(mnConfig.m, mnConfig.n, mnConfig.k);
  mm.SetSingleShape(curSingleM, curSingleN, mnConfig.k);
  mm.SetTensorA(xGm[xOffset]);
  mm.SetTensorB(weightGm[wOffset]);
  if (hasBias) {
    biasGm.SetGlobalBuffer(GetTensorAddr<BiasT>(groupIdx, biasTensorPtr));
    mm.SetBias(biasGm[tailN]);
  }
  mm.template IterateAll<sync>(yGm[outOffset], 0);
}

template <typename mmType, bool sync>
__aicore__ inline void GroupedMatmulCompute<mmType, sync>::MMSync(bool waitIterateAll, bool &mmWaitStatus,
                                                                  bool &firstMM) {
  if (mmWaitStatus) {
    mm.WaitIterateAll();
    mm.End();
    mmWaitStatus = false;
  }
  if (unlikely(firstMM)) {
    firstMM = false;
  } else {
    if (waitIterateAll) {
      SyncAll<true>();
    }
  }
}
}  // namespace GROUPED_MATMUL

#endif  // MS_KERNELS_INTERNAL_KERNEL_ASCENDC_GROUPED_MATMUL_H_
