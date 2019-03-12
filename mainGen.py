
from generator.animatescreen import AnimateScreen as AnimateScreen
from generator.renderscreens import RenderScreens as RenderScreens      
if __name__=='__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--directory', type=str, default='/Users/sameriksson/temp/screensgen/')
    parser.add_argument('--numberOfScreens', type=int, default=10000)
    parser.add_argument('--numberOfItemsOnScreenMax', type=int, default=3)
    parser.add_argument('--numberOfItemsOnScreenMin', type=int, default=1)
    parser.add_argument('--dpi', type=int, default=80)
    parser.add_argument('--widthInches', type=int, default=6)
    parser.add_argument('--heightInches', type=int, default=6)
    parser.add_argument('--animate', type=bool, default=False)
    parser.add_argument('--testScreen', type=bool, default=False)
    parser.add_argument('--randomScreen', type=bool, default=True)
    parser.add_argument('--jitterlow', type=int, default=-20)
    parser.add_argument('--jitterhigh', type=int, default=20)
    parser.add_argument('--incrementer', type=int, default=3)
    parser.add_argument('--cleanupcycles', type=int, default=10000)
    parser.add_argument('--render', type=bool, default=False)
    args = parser.parse_args()
    if args.animate:
        anim= AnimateScreen(args.directory, args.numberOfItemsOnScreenMax,
                    args.numberOfItemsOnScreenMin, args.dpi, args.widthInches,
                    args.heightInches,
                    args.jitterlow, args.jitterhigh, args.incrementer, args.cleanupcycles)
        anim.call_animation()
    else:
        a = RenderScreens(args.directory, args.numberOfScreens, args.numberOfItemsOnScreenMax,
                    args.numberOfItemsOnScreenMin, args.dpi, args.widthInches,
                    args.heightInches, args.testScreen, args.randomScreen,
                    args.jitterlow, args.jitterhigh, args.incrementer, args.cleanupcycles, args.render)
        a.renderScreens()

    