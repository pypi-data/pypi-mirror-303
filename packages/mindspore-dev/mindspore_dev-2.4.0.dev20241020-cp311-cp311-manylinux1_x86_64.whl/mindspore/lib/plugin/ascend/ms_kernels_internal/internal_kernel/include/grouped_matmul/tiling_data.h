#ifndef __GROUPED_MATMUL_TILING_DATA_H__
#define __GROUPED_MATMUL_TILING_DATA_H__

#include <cstdint>
#include <cstring>

#include "kernel_tiling/kernel_tiling.h"

constexpr uint16_t MAX_TENSOR_CONT = 128;

#pragma pack(1)
struct GroupedMatmulBaseParams {
  uint32_t groupNum = 0;
  uint32_t coreNum = 0;
  uint32_t activeType = 0;
  uint32_t ubBaseM = 0;
  uint32_t ubBaseN = 0;
  uint32_t ubCalSize = 0;
  uint32_t ubRestBytes = 0;
  uint32_t workspaceSize = 0;
  int32_t mList[MAX_TENSOR_CONT] = {};
  int32_t kList[MAX_TENSOR_CONT] = {};
  int32_t nList[MAX_TENSOR_CONT] = {};
};
#pragma pack()

#pragma pack(1)
struct GroupedMatmulCtxParams {
  uint32_t tilingKey = 0;
  uint32_t blockDim = 0;
  uint32_t blockDim2 = 0;
  uint32_t blockDim3 = 0;
  uint32_t blockDim4 = 0;
  uint32_t blockDim5 = 0;
  uint32_t blockDim6 = 0;
  uint32_t blockDim7 = 0;
  uint32_t blockDim8 = 0;
};
#pragma pack()

#pragma pack(1)
struct GroupedMatmulTilingData {
  GroupedMatmulBaseParams groupedMatmulBaseParams;
  TCubeTiling mmTilingData;
  GroupedMatmulCtxParams gmmCtxParams;
};
#pragma pack()

#undef GET_TILING_DATA
#define GET_TILING_DATA(tiling_data, tiling_arg) \
  GroupedMatmulTilingData tiling_data;           \
  InitGroupedMatmulTilingData(tiling_arg, &tiling_data)

#endif
