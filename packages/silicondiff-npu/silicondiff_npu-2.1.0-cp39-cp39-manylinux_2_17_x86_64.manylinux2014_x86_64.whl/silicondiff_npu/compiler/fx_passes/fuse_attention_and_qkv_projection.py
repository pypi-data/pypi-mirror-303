from typing import List

import torch
import torch_npu
import silicondiff_npu

from ..utils import replace_pattern_with_filters

aten = torch.ops.aten


def fx_pass_fuse_attention_and_qkv_projection(
    gm: torch.fx.GraphModule, example_inputs: List[torch.Tensor]
) -> torch.fx.GraphModule:
    for mm in [aten.matmul.default, aten.mm.default]:
        # cross attention
        def pattern0(
            q: torch.Tensor,
            wq: torch.Tensor,
            kv: torch.Tensor,
            wk: torch.Tensor,
            wv: torch.Tensor,
            num_heads: int,
            scale_value: float,
        ):
            query = mm(q, wq)
            key = mm(kv, wk)
            value = mm(kv, wv)

            out = torch_npu.npu_prompt_flash_attention(
                query,
                key,
                value,
                num_heads=num_heads,
                scale_value=scale_value,
                input_layout="BSH",
            )
            return out

        def replacement0(
            q: torch.Tensor,
            wq: torch.Tensor,
            kv: torch.Tensor,
            wk: torch.Tensor,
            wv: torch.Tensor,
            num_heads: int,
            scale_value: float,
        ):
            return silicondiff_npu.ops.fused_qkv_projection_and_attention(
                q, kv, kv, wq, wk, wv, num_heads=num_heads, scale_value=scale_value
            )

        # self attention
        def pattern1(
            qkv: torch.Tensor,
            wq: torch.Tensor,
            wk: torch.Tensor,
            wv: torch.Tensor,
            num_heads: int,
            scale_value: float,
        ):
            query = mm(qkv, wq)
            key = mm(qkv, wk)
            value = mm(qkv, wv)

            out = torch_npu.npu_prompt_flash_attention(
                query,
                key,
                value,
                num_heads=num_heads,
                scale_value=scale_value,
                input_layout="BSH",
            )
            return out

        def replacement1(
            qkv: torch.Tensor,
            wq: torch.Tensor,
            wk: torch.Tensor,
            wv: torch.Tensor,
            num_heads: int,
            scale_value: float,
        ):
            return silicondiff_npu.ops.fused_qkv_projection_and_attention(
                qkv, qkv, qkv, wq, wk, wv, num_heads=num_heads, scale_value=scale_value
            )

        # cross attention
        def pattern2(
            q: torch.Tensor,
            wq: torch.Tensor,
            kv: torch.Tensor,
            wk: torch.Tensor,
            wv: torch.Tensor,
            num_heads: int,
            num_key_value_heads: int,
            scale_value: float,
            shape_0: List[int],
            shape_1: List[int],
            shape_2: List[int],
            shape: List[int],
        ):
            query = mm(q, wq)
            key = mm(kv, wk)
            value = mm(kv, wv)

            reshape_query = aten.reshape.default(query, shape_0)
            transpose_query = aten.transpose.int(reshape_query, 1, 2)
            reshape_key = aten.reshape.default(key, shape_1)
            transpose_key = aten.transpose.int(reshape_key, 1, 2)
            reshape_value = aten.reshape.default(value, shape_2)
            transpose_value = aten.transpose.int(reshape_value, 1, 2)

            query = aten.contiguous.default(transpose_query)
            key = aten.contiguous.default(transpose_key)
            value = aten.contiguous.default(transpose_value)

            out = torch_npu.npu_prompt_flash_attention(
                query,
                key,
                value,
                num_heads=num_heads,
                scale_value=scale_value,
                next_tokens=65535,
                input_layout="BNSD",
                num_key_value_heads=num_key_value_heads,
            )
            transpose_out = aten.transpose.int(out, 1, 2)
            reshape_out = aten.reshape.default(transpose_out, shape)
            return reshape_out

        def replacement2(
            q: torch.Tensor,
            wq: torch.Tensor,
            kv: torch.Tensor,
            wk: torch.Tensor,
            wv: torch.Tensor,
            num_heads: int,
            num_key_value_heads: int,
            scale_value: float,
            shape_0: List[int],
            shape_1: List[int],
            shape_2: List[int],
            shape: List[int],
        ):
            return silicondiff_npu.ops.fused_qkv_projection_and_attention(
                q, kv, kv, wq, wk, wv, num_heads=num_heads, scale_value=scale_value
            )

        # self attention
        def pattern3(
            qkv: torch.Tensor,
            wq: torch.Tensor,
            wk: torch.Tensor,
            wv: torch.Tensor,
            num_heads: int,
            num_key_value_heads: int,
            scale_value: float,
            shape_0: List[int],
            shape_1: List[int],
            shape_2: List[int],
            shape: List[int],
        ):
            query = mm(qkv, wq)
            key = mm(qkv, wk)
            value = mm(qkv, wv)

            reshape_query = aten.reshape.default(query, shape_0)
            transpose_query = aten.transpose.int(reshape_query, 1, 2)
            reshape_key = aten.reshape.default(key, shape_1)
            transpose_key = aten.transpose.int(reshape_key, 1, 2)
            reshape_value = aten.reshape.default(value, shape_2)
            transpose_value = aten.transpose.int(reshape_value, 1, 2)

            query = aten.contiguous.default(transpose_query)
            key = aten.contiguous.default(transpose_key)
            value = aten.contiguous.default(transpose_value)

            out = torch_npu.npu_prompt_flash_attention(
                query,
                key,
                value,
                num_heads=num_heads,
                scale_value=scale_value,
                next_tokens=65535,
                input_layout="BNSD",
                num_key_value_heads=num_key_value_heads,
            )
            transpose_out = aten.transpose.int(out, 1, 2)
            reshape_out = aten.reshape.default(transpose_out, shape)
            return reshape_out

        def replacement3(
            qkv: torch.Tensor,
            wq: torch.Tensor,
            wk: torch.Tensor,
            wv: torch.Tensor,
            num_heads: int,
            num_key_value_heads: int,
            scale_value: float,
            shape_0: List[int],
            shape_1: List[int],
            shape_2: List[int],
            shape: List[int],
        ):
            return silicondiff_npu.ops.fused_qkv_projection_and_attention(
                qkv, qkv, qkv, wq, wk, wv, num_heads=num_heads, scale_value=scale_value
            )

        for pattern, replacement in [
            (pattern0, replacement0),
            (pattern1, replacement1),
            (pattern2, replacement2),
            (pattern3, replacement3),
        ]:
            gm = replace_pattern_with_filters(
                gm,
                pattern,
                replacement,
                match_filters=[],
                name="fuse_cross_attention_and_qkv_projection",
            )

    return gm
