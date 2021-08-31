
"""
This extension add scoreboard and liveboard
"""


from campy.gui.events.timer import pause
from breakoutGraphics_extention import BreakoutGraphics

FRAME_RATE = 1000 / 120  # 120 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics(number_lives=NUM_LIVES)
    count_lives = 0  # number of out_ball
    count_bricks = 0  # number of bricks player hit
    # Add animation loop here!
    while True:
        pause(FRAME_RATE)
        graphics.ball.move(graphics.get_dx(), graphics.get_dy())
        if graphics.ball_hit_thing() is not None:  # hit the paddle or brick
            if graphics.ball_hit_thing() is not graphics.paddle:  # hit the brick
                graphics.chang_dy_direction()
                graphics.window.remove(graphics.ball_hit_thing())
                count_bricks += 1
                graphics.scoreboard.text = 'Score: '+str(count_bricks)
                if count_bricks == graphics.bricks_number:  # clear all bricks
                    break
            else:  # hit the paddle
                if graphics.get_dy() > 0:  # makes ball do not stick on the paddle
                    graphics.chang_dy_direction()
        if graphics.ball.x <= 0 or graphics.ball.x + graphics.r * 2 >= graphics.window.width:
            # between two sides of window
            graphics.chang_dx_direction()
        if graphics.ball.y <= 0:  # up_side of window
            graphics.chang_dy_direction()
        if graphics.ball.y >= graphics.window.height:  # ball is out of window
            graphics.reset_ball()
            count_lives += 1
            graphics.liveboard.text = graphics.remain_lives(count_lives, NUM_LIVES)
            graphics.window.add(graphics.liveboard, graphics.window.width - graphics.liveboard.width,
                                graphics.liveboard.height)
            if count_lives == NUM_LIVES:
                graphics.liveboard.text = 'Game Over!'
                graphics.window.add(graphics.liveboard, graphics.window.width - graphics.liveboard.width,
                                    graphics.liveboard.height)
                break



if __name__ == '__main__':
    main()