import struct
import cocotb


def swap(hex_data, alignment=32, swapon=True):
    if not swapon:
        x0 = int(hex_data, 16).to_bytes(alignment//8, byteorder="little")[::-1]
        x1 = int.from_bytes(x0, 'little')
        x2 = ((0xffffffff & x1) << 32) | x1 >> 32
        cocotb.log.info(f"swap hex data= {hex_data} {x0} {hex(x1)}")
        return x2
    if (alignment == 64):
        return struct.unpack("<Q", struct.pack(">Q", int(hex_data, 16)))[0]
    else:
        return struct.unpack("<I", struct.pack(">I", int(hex_data, 16)))[0]


def get_hex_code(filename, alignment=32, swapon=True):
    with open(filename,'r') as file:
        Lines = file.readlines()
        file.close()
        # Strips the newline character
        address = []
        instr_code = {}
        # Read hex file line by line and separate out the addresses & hex data
        for line in Lines:
            if "@" in line:
                address1 = line[1:len(line.strip())]
                # print("address:",address1)
                address.append(('0x'+address1))
                address_str = str('0x'+address1)
                instr_code[address_str] = []
            else:
                for hex_code in line.split():
                    instr_code[address_str].append(hex_code)
        # Generate the hex value of the instruction code
        hex_code = {}
        for instr_code_addr, instr_code_data in instr_code.items():
            instr_code_addr_int = int(instr_code_addr, 16)
            instr_code_addr_hex_value = hex(instr_code_addr_int)
            hex_code[instr_code_addr_hex_value] = []
            for instr_code_data_string in instr_code_data:
                hex_code[instr_code_addr_hex_value].append(
                    hex(int(instr_code_data_string, 16)))
            # print(hex_code)
        addr_all = []
        hex_data_all = []
        hex_data_all1 = []
        mram_hex_code = {}
        # Generate the hex value of the address
        for addr in hex_code.keys():
            cnt = 0
            for hex_data in hex_code[addr]:
                addr1 = hex(int(addr, 16) + 8 * cnt)
                cnt += 1
                addr_all.append(addr1)
                if (alignment == 64):
                    hex_data1 = hex_data
                    hex_data1 = swap(hex_data1, alignment, swapon)
                    hex_data_all1.append(hex(hex_data1))
                hex_data_all.append(hex_data)
        # print("address_all: ",addr_all)
        if (alignment == 64):
            mram_hex_code['address'] = addr_all
            mram_hex_code['data'] = hex_data_all1
            print(mram_hex_code)
            return mram_hex_code
        # Generate the 4 byte aligned address
        tcm_hex_code = {}
        addr_value_all = []
        for addr in addr_all:
            for i in range(2):
                addr = str(addr)
                addr = hex(int(addr, 16)+int(str(hex(i*4)), 16))
                addr_value_all.append(addr)
        # print(addr_value_all)
        tcm_hex_code['address'] = addr_value_all
        # Generate the 4 byte aligned data
        hex_data_value_all = []
        for hex_data in hex_data_all:
            for i in range(2):
                hex_data1 = str(hex_data)
                if (not i):
                    hex_data1 = hex(
                        (int(hex_data1, 16) & 0xffffffff00000000) >> 32)
                    hex_data11 = swap(hex_data1, alignment, swapon)
                    hex_data_value_all.append(hex(hex_data11))
                else:
                    hex_data1 = hex(int(hex_data1, 16) & 0x00000000ffffffff)
                    hex_data11 = swap(hex_data1, alignment, swapon)
                    hex_data_value_all.append(hex(hex_data11))
        print(hex_data_value_all)
        # put all address and data in one dict and return it
        tcm_hex_code['data'] = hex_data_value_all
        return tcm_hex_code
