import sys
import argparse
import caesarCoder
import vigenereCoder

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(dest='modeName')

parserEncode = subparsers.add_parser('encode')
parserEncode.add_argument('--cipher', choices=["ceasar", "vigenere"], required=True)
parserEncode.add_argument('--key', required=True)

parserDecode = subparsers.add_parser('decode')
parserDecode.add_argument('--cipher', choices=["ceasar", "vigenere"], required=True)
parserDecode.add_argument('--key', required=True)

parserTrain = subparsers.add_parser('train')
parserTrain.add_argument('--model-file', type=str, required=True)

parserHack = subparsers.add_parser('hack')
parserHack.add_argument('--model-file', type=str, required=True)

parser.add_argument('--input-file', type=str)
parser.add_argument('--output-file', type=str)

args = parser_args()


