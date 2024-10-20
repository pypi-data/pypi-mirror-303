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

#ifndef MS_KERNELS_INTERNAL_KERNEL_GROUPED_MATMUL_TILING_H_
#define MS_KERNELS_INTERNAL_KERNEL_GROUPED_MATMUL_TILING_H_

#include <algorithm>
#include <numeric>
#include "graph/types.h"
#include "include/ms_int_types.h"
#include "tiling_data.h"
#include "internal_kernel.h"
#include "matrix/matmul_tiling.h"
#include "utils/log/log.h"

using namespace ge;
// using namespace AscendC;
using namespace mindspore::internal;

namespace grouped_matmul_optiling {
constexpr uint32_t X_INDEX = 0;
constexpr uint32_t WEIGHT_INDEX = 1;
constexpr uint32_t BIAS_INDEX = 2;
constexpr int64_t BEST_L1_PARTA = 256 * 1024;
constexpr int64_t BEST_L1_PARTB = 128 * 1024;
constexpr int64_t BEST_BASEN = 256;
constexpr uint32_t UB_DIVIDE_NUM = 2;
constexpr uint32_t UB_BLOCK_UNIT_SIZE = 32;  // 32: a block has 32 bytes data
constexpr uint32_t UB_ANTIQUANT_PER_BLOCK_ALIGN = 4 * 1024;
constexpr uint32_t UB_ANTIQUANT_BLOCK_NUM_FP16 = 6;
constexpr uint32_t UB_ANTIQUANT_IO_USED_BLOCK_FP16 = 6;
constexpr uint32_t UB_ANTIQUANT_BLOCK_NUM_BF16 = 8;  // tmpUb used 2 blks
constexpr uint32_t UB_ANTIQUANT_IO_USED_BLOCK_BF16 = 6;
constexpr uint32_t QUEUE_DOUBLE_BUFFER = 2;
constexpr uint32_t FP32_DATATYPE_SIZE = 4;
constexpr uint32_t INVERSE_FIFTEEN = ~15;
constexpr uint64_t TILING_KEY = 0;
constexpr uint64_t DOUBLE_BUFFER_L0A_L0B = 2;
constexpr uint64_t DOUBLE_BUFFER_STEPKA_STEPKB = 2;
constexpr uint32_t SYS_WORKSPACE_SIZE = 16 * 1024 * 1024;
constexpr int32_t MAX_INT32 = 2147483647;

inline uint32_t SixteenAlign(uint32_t a) {
  // 16向下对齐
  return a & INVERSE_FIFTEEN;
}

class GroupedMatmulTilingCtx {
 public:
  GroupedMatmulTilingCtx(std::string nodeName, std::vector<Tensor *> inputs, std::vector<Tensor *> outputs,
                         GroupedMatmulTilingData *tilingData)
      : nodeName_(nodeName), inputs_(inputs), outputs_(outputs), tilingData_(tilingData) {
    // current the last input shape contains the infomation of dyn_input_list_
    auto last_input_shape = inputs_[inputs_.size() - 1]->desc.dims;
    dyn_input_list_.resize(last_input_shape.size());
    for (size_t i = 0; i < last_input_shape.size(); ++i) {
      dyn_input_list_[i] = last_input_shape[i];
      MSOP_LOG(INFO) << "dyn_input_list_ [" << i << "]: " << dyn_input_list_[i];
    }
    real_input_num_ = std::accumulate(dyn_input_list_.begin(), dyn_input_list_.end(), 0);
    real_output_num_ = dyn_input_list_[0];
  }
  ~GroupedMatmulTilingCtx() {}

  Tensor *GetOptionalInputTensor(uint32_t index) const {
    if (index >= real_input_num_) {
      return nullptr;
    }
    return inputs_[index];
  }

  Tensor *GetDynamicInputTensor(uint32_t index, uint32_t list_i = 0) const {
    if (index >= dyn_input_list_.size()) {
      return nullptr;
    }
    if (list_i >= dyn_input_list_[index]) {
      return nullptr;
    }
    int pre_offset = std::accumulate(dyn_input_list_.begin(), dyn_input_list_.begin() + index, 0);
    return pre_offset + list_i >= real_input_num_ ? nullptr : inputs_[pre_offset + list_i];
  }

  Tensor *GetOptionalOutputTensor(uint32_t index) const {
    if (index >= real_output_num_) {
      return nullptr;
    }
    return outputs_[index];
  }

  TensorDesc *GetOptionalInputDesc(uint32_t index) const {
    auto tensor = GetOptionalInputTensor(index);
    return tensor ? &(tensor->desc) : nullptr;
  }

  TensorDesc *GetDynamicInputDesc(uint32_t index, uint32_t list_i = 0) const {
    auto tensor = GetDynamicInputTensor(index, list_i);
    return tensor ? &(tensor->desc) : nullptr;
  }

  TensorDesc *GetInputDesc(uint32_t index) const {
    auto tensor = GetOptionalInputTensor(index);
    return tensor ? &(tensor->desc) : nullptr;
  }

  TensorDesc *GetOutputDesc(uint32_t index) const {
    auto tensor = GetOptionalOutputTensor(index);
    return tensor ? &(tensor->desc) : nullptr;
  }

  DIMS GetInputShape(uint32_t index) const {
    DIMS empty;
    auto tensor = GetOptionalInputTensor(index);
    return tensor ? tensor->desc.dims : empty;
  }

  std::string GetNodeName() const { return nodeName_; }

  void SetTilingKey(uint32_t key) { tilingData_->gmmCtxParams.tilingKey = key; }

  void SetBlockDim(uint32_t blockDim) { tilingData_->gmmCtxParams.blockDim = blockDim; }

 public:
  std::string nodeName_;
  std::vector<Tensor *> inputs_;
  std::vector<Tensor *> outputs_;
  GroupedMatmulTilingData *tilingData_;
  size_t workspace_size_;
  std::vector<int32_t> dyn_input_list_{};
  int32_t real_input_num_{0};
  int32_t real_output_num_{0};
};

class GroupedMatmulTiling {
 public:
  GroupedMatmulTilingData *tilingData;
  int Init(const GroupedMatmulTilingCtx *context);
  int RunFusionKernelTiling(GroupedMatmulTilingCtx *context);

 protected:
  int CalMMTiling(const GroupedMatmulTilingCtx *context, matmul_tiling::PlatformInfo info);
  int GroupedMatmulSetMMTiling(const GroupedMatmulTilingCtx *context, uint64_t l1Size, uint64_t l0CSize,
                               matmul_tiling::DataType matmulDtype);
  int GroupedMatmulCalUbSize(const GroupedMatmulTilingCtx *context, uint32_t ubSize, uint32_t divideBlkNum,
                             uint32_t ioBlkNum, uint32_t ubBlockAlign);

 private:
  uint32_t ubBaseM;
  uint32_t ubBaseN;
  int32_t maxM;
  int32_t maxN;
  int32_t maxK;
  int32_t baseM_;
  int32_t baseN_;
  int32_t baseK_;
  uint64_t ubSize_;
  uint32_t mmDataTypeSize;
  uint32_t ubCalSize;
  uint32_t ubRestBytes;
  uint32_t ubDivideBlkNum = 0;
  uint32_t ubIoBlkNum = 0;
  uint32_t ubBlockAlign = 0;
  uint32_t groupNum;
  uint32_t workspacesSize;  // for antiquant

  ge::DataType mmDType;
  ge::DataType weightDtype;
  ge::DataType biasDType;
  matmul_tiling::PlatformInfo info;
  std::string soc_{"Ascend910B4"};
};

}  // namespace grouped_matmul_optiling

#endif
