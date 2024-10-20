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

#ifndef GROUPED_MATMUL_INTERFACE_H
#define GROUPED_MATMUL_INTERFACE_H

void grouped_matmul_do(uint32_t blockDim, void *l2ctrl, void *stream, uint8_t *x, uint8_t *weight, uint8_t *bias,
                       uint8_t *scale, uint8_t *offset, uint8_t *antiquantScale, uint8_t *antiquantOffset,
                       uint8_t *group_list, uint8_t *y, uint8_t *workspace, uint8_t *tiling);

#endif  // GROUPED_MATMUL_INTERFACE_H
