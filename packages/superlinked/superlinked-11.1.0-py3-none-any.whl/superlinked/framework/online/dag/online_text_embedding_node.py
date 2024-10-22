# Copyright 2024 Superlinked, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import annotations

from beartype.typing import Sequence, cast
from typing_extensions import override

from superlinked.framework.common.dag.context import ExecutionContext
from superlinked.framework.common.dag.text_embedding_node import TextEmbeddingNode
from superlinked.framework.common.data_types import Vector
from superlinked.framework.common.embedding.sentence_transformer_embedding import (
    SentenceTransformerEmbedding,
)
from superlinked.framework.common.interface.has_embedding import HasEmbedding
from superlinked.framework.common.interface.has_length import HasLength
from superlinked.framework.common.parser.parsed_schema import ParsedSchema
from superlinked.framework.common.storage_manager.storage_manager import StorageManager
from superlinked.framework.online.dag.default_online_node import DefaultOnlineNode
from superlinked.framework.online.dag.evaluation_result import (
    EvaluationResult,
    SingleEvaluationResult,
)
from superlinked.framework.online.dag.online_node import OnlineNode


class OnlineTextEmbeddingNode(
    DefaultOnlineNode[TextEmbeddingNode, Vector], HasLength, HasEmbedding
):
    def __init__(
        self,
        node: TextEmbeddingNode,
        parents: list[OnlineNode],
        storage_manager: StorageManager,
    ) -> None:
        super().__init__(node, parents, storage_manager)
        self._embedding = self._init_embedding()

    @property
    @override
    def length(self) -> int:
        return self.node.length

    @property
    @override
    def embedding(self) -> SentenceTransformerEmbedding:
        return self._embedding

    def _init_embedding(self) -> SentenceTransformerEmbedding:
        return cast(SentenceTransformerEmbedding, self.node.init_embedding())

    @override
    def evaluate_self(
        self,
        parsed_schemas: list[ParsedSchema],
        context: ExecutionContext,
    ) -> list[EvaluationResult[Vector]]:
        if context.should_load_default_node_input:
            result = EvaluationResult(
                self._get_single_evaluation_result(self.embedding.default_vector)
            )
            return [result] * len(parsed_schemas)
        return super().evaluate_self(parsed_schemas, context)

    @override
    def _evaluate_singles(
        self,
        parent_results: list[dict[OnlineNode, SingleEvaluationResult]],
        context: ExecutionContext,
    ) -> Sequence[Vector | None]:
        none_indices = [
            i for i, parent_result in enumerate(parent_results) if not parent_result
        ]
        non_none_parent_results = [
            parent_result for parent_result in parent_results if parent_result
        ]
        input_ = list(
            map(
                lambda parent_result: list(parent_result.values())[0].value,
                non_none_parent_results,
            )
        )
        embedded_texts: list[Vector | None] = list(self.__embed_texts(input_, context))
        for i in none_indices:
            embedded_texts.insert(i, None)
        return embedded_texts

    def __embed_texts(
        self, texts: Sequence[str], context: ExecutionContext
    ) -> list[Vector]:
        return self.embedding.embed_multiple(texts, context)
