from alldigitalradio.io.xilinx_gtp import XilinxGTPSerdes
from nmigen.build import Resource, Pins, Attrs

def load():
    from boards.qmtech_wukong import Platform as wukong

    wukong.resources += [
        Resource("clk_n", 0, Pins("AB13", dir="i")),
        Resource("clk_p", 0, Pins("AA13", dir="i")), 

        Resource("tx_n", 0, Pins("AD10")),
        Resource("tx_p", 0, Pins("AC10")),

        Resource("rx_n", 0, Pins("AD12")),
        Resource("rx_p", 0, Pins("AC12"))
    ]

    return (wukong, XilinxGTPSerdes)
