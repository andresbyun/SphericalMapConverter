import sys
import argparse

# Main function
def main(argv):
    
    print(argv[1])

if __name__ == "__main__":
    # TODO: Process arguments and then send to main
    # for now just focus on input and output flags
    parser = argparse.ArgumentParser(description='Transform input image into Equirectangular/Spherical projection')
    parser.add_argument('input', help='input filename', metavar='input', required=True)

    main(sys.argv)
