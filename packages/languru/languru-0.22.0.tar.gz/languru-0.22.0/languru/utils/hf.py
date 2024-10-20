from typing import Literal, Optional, Sequence, Text, Union, cast

import torch
from transformers import PreTrainedTokenizer, PreTrainedTokenizerFast, StoppingCriteria


def remove_special_tokens(
    text: Text, tokenizer: Union[PreTrainedTokenizer, PreTrainedTokenizerFast]
) -> Text:
    """Remove special tokens from the text.

    Parameters
    ----------
    text: Text
        The text to remove special tokens from.

    Returns
    -------
    Text
        The text with special tokens removed.
    """

    return tokenizer.decode(tokenizer.encode(text), skip_special_tokens=True)


class StopAtWordsStoppingCriteria(StoppingCriteria):

    def __init__(self, stop_words_ids: Sequence["torch.LongTensor"]):
        """Create a stopping criteria that stops when the model generates a
        sequence of tokens that matches any of the stop words.

        Parameters
        ----------
        stop_words_ids: Sequence["torch.LongTensor"]
            A sequence of token ids to stop at. e.g.:
            [tensor(50256), tensor([  58,   47, 2885,   60])]
        """

        super().__init__()

        self.stop_words_ids = [self.to_cpu_long(s) for s in stop_words_ids]
        self.stop_reason: Optional[Literal["stop", "length", "content_filter"]] = None

    def __call__(self, input_ids: "torch.LongTensor", scores: "torch.FloatTensor"):
        input_ids_cpu = self.to_cpu_long(input_ids)
        for stop_words_id in self.stop_words_ids:
            if torch.all(
                (stop_words_id == input_ids_cpu[0][-len(stop_words_id) :])
            ).item():
                self.stop_reason = "stop"
                return True
        return False

    def get_stop_reason(self) -> Optional[Literal["stop", "length", "content_filter"]]:
        return self.stop_reason

    def to_cpu_long(self, tensor: "torch.Tensor") -> "torch.LongTensor":
        long_tensor = tensor.cpu().long()
        long_tensor = cast(torch.LongTensor, long_tensor)
        return long_tensor

    @classmethod
    def from_stop_words(
        cls,
        stop_words: Sequence[Text],
        tokenizer: Union["PreTrainedTokenizer", "PreTrainedTokenizerFast"],
    ) -> "StopAtWordsStoppingCriteria":
        """Create a stopping criteria from a sequence of stop words.

        Parameters
        ----------
        stop_words: Sequence[Text]
            A sequence of stop words. e.g.: ["[END]", "[STOP]"
        tokenizer: PreTrainedTokenizer | PreTrainedTokenizerFast
            A tokenizer to convert the stop words to token ids.

        Returns
        -------
        StopAtWordsStoppingCriteria
            A stopping criteria that stops when the model generates
            a sequence of tokens that matches any of the stop words.
        """

        if not stop_words:
            raise ValueError("The `stop_words` cannot be empty")

        stop_words_ids = []
        for stop_word in stop_words:
            _input_ids = tokenizer(stop_word, return_tensors="pt")["input_ids"]
            _input_ids = cast(torch.LongTensor, _input_ids)
            each_stop_words_ids = _input_ids.squeeze()
            stop_words_ids.append(each_stop_words_ids)

        return cls(stop_words_ids=stop_words_ids)
