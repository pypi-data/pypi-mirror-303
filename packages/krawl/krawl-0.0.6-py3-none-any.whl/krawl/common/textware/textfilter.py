import re
from typing import List


class TextFilter:

    @staticmethod
    def corepart(
        text: str,
        window_size: int = 5,
        core_window: int = 7
    ) -> str:
        """Find the core part of the text.
        """
        lines = text.split("\n")
        if len(lines) > window_size:
            # Find line at the largest moving average
            line_size = [len(re.sub(r'\W', '', line)) for line in lines]
            moving_avg = [sum(line_size[idx:idx+window_size])
                          for idx in range(len(line_size)-window_size)]
            max_idx = moving_avg.index(max(moving_avg))
            # Potential end signal
            empty_parts = [
                1 if (size <= window_size) else
                0 for size in moving_avg
            ]
            empty_idx = empty_parts.index(1) if sum(empty_parts) else 1e6
            start = max_idx
            end = start + min(core_window, empty_idx)
        else:
            start = 0
            end = window_size
        core = "\n".join(lines[start:end])
        return core

    @staticmethod
    def remove_noise_in_seq(
        text_seq: List[str],
        min_line_len: int = 3,
        nchar_real_line: int = 36,
        max_line_count: int = 300
    ) -> str:
        """Remove contextual noise from the text.

        Parameters
        ----------
        text : str
            Normally the `text extracted from a webpage`. It can thus contain
            - text from navigation bars
            - text from footers
            - strange links
            - etc.
        max_char_len : int, optional
            _description_, by default 2000
        min_paragraph_len : int, optional
            _description_, by default 3
        """
        # Drop obvious bad lines
        lines = [
            line for line in text_seq if (
                len(line) >= min_line_len
            )
        ]

        # Identify the start of real content
        # TODO: use nchar of all lines + moving average of x-lines
        line_size = [len(line) for line in lines]
        start_idx = 0
        for idx, size in enumerate(line_size):
            start_idx = idx
            if size >= nchar_real_line:
                break

        start_idx = max(0, start_idx-1)
        end_idx = start_idx + max_line_count
        lines = lines[start_idx:end_idx]

        return "\n".join(lines)

    @staticmethod
    def remove_noise(
        text: str,
        min_line_len: int = 3,
        nchar_real_line: int = 36,
        max_line_count: int = 300
    ) -> str:
        """Remove contextual noise from the text.
        """
        lines = text.split("\n")
        return TextFilter.remove_noise_in_seq(
            text_seq=lines,
            min_line_len=min_line_len,
            nchar_real_line=nchar_real_line,
            max_line_count=max_line_count
        )
