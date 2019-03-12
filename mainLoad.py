from render.jsonloader import JsonLoader as JsonLoader
from render.render import Render as Render
if __name__=='__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--directory', type=str, default='/Users/sameriksson/temp/screensgen/')
    parser.add_argument('--save', type=bool, default=True)
    args = parser.parse_args()
    rend = Render(args.directory)
    rend.render(args.save)