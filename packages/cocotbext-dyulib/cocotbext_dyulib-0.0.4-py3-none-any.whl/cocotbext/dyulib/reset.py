import cocotb
from cocotb.triggers import Timer, RisingEdge, Event

reset_start = Event()
clock_in_reset_start = Event()
clock_in_reset_stop = Event()
reset_end = Event()


async def reset_n(
    clk,
    rst_n,
    wait_time=(1, "ns"),
    reset_time=(100, "ns"),
    clock_cycles_in_reset=0,
    post_clock_quiet_time=(0, "ns"),
    active_low=True
):
    if active_low:
        rst = 0
        norst = 1
    else:
        rst = 1
        norst = 0
    rst_n.value = norst
    await Timer(wait_time[0], wait_time[1])
    rst_n.value = rst
    reset_start.set()
    await Timer(reset_time[0], reset_time[1])
    if clock_cycles_in_reset > 0:
        clock_in_reset_start.set()
        for _ in range(clock_cycles_in_reset):
            await RisingEdge(clk)
        clock_in_reset_stop.set()
        if post_clock_quiet_time[0] > 0:
            await Timer(post_clock_quiet_time[0], post_clock_quiet_time[1])
    rst_n.value = norst
    reset_end.set()
