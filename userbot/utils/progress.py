# Copyright (C) 2021 Farid Dadashzade
# Telegram: @Faridxz
#

import math
import time

from .exceptions import CancelProcess
from .tools import humanbytes, time_formatter


async def progress(
    current, total, gdrive, start, prog_type, file_name=None, is_cancelled=False
):
    now = time.time()
    diff = now - start
    if is_cancelled is True:
        raise CancelProcess

    if round(diff % 10.00) == 0 or current == total:
        percentage = current * 100 / total
        speed = current / diff
        elapsed_time = round(diff)
        eta = round((total - current) / speed)
        if "upload" in prog_type.lower():
            status = "Hazırlanır...\nBiraz gözləyin."
        elif "download" in prog_type.lower():
            status = "Yüklənir..\nBiraz gözləyin..."
        else:
            status = "Bilinməyən"
        progress_str = "`{}` | [{}{}] `{}%`".format(
            status,
            "".join("●" for i in range(math.floor(percentage / 10))),
            "".join("○" for i in range(10 - math.floor(percentage / 10))),
            round(percentage, 2),
        )

        tmp = (
            f"{progress_str}\n"
            f"`{humanbytes(current)} of {humanbytes(total)}"
            f" @ {humanbytes(speed)}`\n"
            f"`ETA` -> {time_formatter(eta)}\n"
            f"`Təxmini` -> {time_formatter(elapsed_time)}"
        )
        await gdrive.edit(f"`{prog_type}`\n\n" f"`C Y B Σ R`\n{tmp}")
