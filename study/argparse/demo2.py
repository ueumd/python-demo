import math
import argparse

def parse_args():
    parse = argparse.ArgumentParser(description="Calculate cylinder volume")
    parse.add_argument("-r", "--radius", type=int, default=2, help="Radius of Cylinder")
    parse.add_argument("--height", type=int, default=4, help="Height of Cylinder")

    args = parse.parse_args()
    return args

def cal_vol(radius, height):
    vol = math.pi * pow(radius, 2) * height
    return  vol


# python demo2.py 2 4
if __name__ == '__main__':
    args = parse_args()
    print(cal_vol(args.radius, args.height))