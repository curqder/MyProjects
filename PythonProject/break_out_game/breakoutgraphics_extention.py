
"""
This extension add scoreboard and liveboard
"""

from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Height of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10        # Number of rows of bricks.
BRICK_COLS = 10        # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10       # Radius of the ball (in pixels).
PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7  # Initial vertical speed for the ball.
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:
    """
    Create objects : window,ball,bricks,paddle,
    define some attribute
    """
    def __init__(self, ball_radius = BALL_RADIUS, paddle_width = PADDLE_WIDTH,
                 paddle_height = PADDLE_HEIGHT, paddle_offset = PADDLE_OFFSET,
                 brick_rows = BRICK_ROWS, brick_cols = BRICK_COLS,
                 brick_width = BRICK_WIDTH, brick_height = BRICK_HEIGHT,
                 brick_offset = BRICK_OFFSET, brick_spacing = BRICK_SPACING,
                 count_lives = 0, number_lives = 3,
                 title='Breakout'):

        self.paddle_width = paddle_width
        self.r = ball_radius
        self.bricks_number = brick_rows * brick_cols

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height,)
        self.paddle.filled = True
        self.window.add(self.paddle, x=(window_width-paddle_width)/2, y=window_height-paddle_offset)

        # Center a filled ball in the graphical window
        self.ball = GOval(2*ball_radius, 2*ball_radius)
        self.ball.filled = True
        self.window.add(self.ball, window_width/2-ball_radius, window_height/2-ball_radius)

        # Default initial velocity for the ball
        self.__dx = 0  # strict private
        self.__dy = 0  # strict private

        # Initialize our mouse listeners
        onmousemoved(self.move_paddle)
        onmouseclicked(self.start_ball)

        # Draw bricks
        for i in range(brick_rows):
            for j in range(brick_cols):
                self.bricks = GRect(brick_width, brick_height)
                self.bricks.filled = True
                if i <= 1:
                    self.bricks.fill_color = 'firebrick'
                if 2 <= i <= 3:
                    self.bricks.fill_color = 'coral'
                if 4 <= i <= 5:
                    self.bricks.fill_color = 'gold'
                if 6 <= i <= 7:
                    self.bricks.fill_color = 'yellowgreen'
                if i > 7:
                    self.bricks.fill_color = 'lightseagreen'
                self.window.add(self.bricks, x=j*(brick_width+brick_spacing),
                                y=brick_offset+i*(brick_height+brick_spacing))
        # Scoreboard
        self.score = 0
        self.scoreboard = GLabel('Score: ' + str(self.score))
        self.scoreboard.font = '-20'
        self.window.add(self.scoreboard, 0, self.scoreboard.height)

        # liveboard
        self.liveboard = GLabel(self.remain_lives(count_lives, number_lives))
        self.liveboard.font = '-20'
        self.window.add(self.liveboard, window_width-self.liveboard.width, self.liveboard.height)


    def move_paddle(self, mouse):
        """
        The paddle will move with the user's mouse,
        and make paddle do not out of the window.
        :param mouse: mouse's information
        """
        if self.paddle_width / 2 < mouse.x < self.window.width - self.paddle_width / 2:
            # between window's two side
            self.paddle.x = mouse.x - self.paddle_width / 2
        elif mouse.x >= self.window.width - self.paddle_width / 2:
            # right side
            self.paddle.x = self.window.width - self.paddle_width
        else:
            # left side
            self.paddle.x = 0

    def start_ball(self, mouse):
        """
        When user click, this function will reset ball's velocity.
        It will check the ball is already moving first.
        : param mouse: mouse's information
        """
        if self.__dx == 0 and self.__dy == 0:  # ball is not moving
            self.__dy = INITIAL_Y_SPEED
            self.__dx = random.randint(1, MAX_X_SPEED)
            if random.random() > 0.5:  # random direction
                self.__dx = - self.__dx

    def get_dx(self):
        # Getter
        return self.__dx

    def get_dy(self):
        # Getter
        return self.__dy

    def ball_hit_thing(self):
        """
        This method check 4 angels of the ball on window.
        : return : object(bricks or paddle) or None
        """
        maybe_object = self.window.get_object_at(self.ball.x, self.ball.y)
        if maybe_object is not None:
            return maybe_object
        maybe_object = self.window.get_object_at(self.ball.x + 2 * self.r, self.ball.y)
        if maybe_object is not None:
            return maybe_object
        maybe_object = self.window.get_object_at(self.ball.x + 2 * self.r, self.ball.y + 2 * self.r)
        if maybe_object is not None:
            return maybe_object
        maybe_object = self.window.get_object_at(self.ball.x, self.ball.y + 2 * self.r)
        if maybe_object is not None:
            return maybe_object

    def reset_ball(self):
        # this method reset ball's position and velocity
        self.window.add(self.ball, self.window.width/2 - self.r, self.window.height/2 - self.r)
        self.__dx = 0
        self.__dy = 0

    def chang_dx_direction(self):
        # Setter
        self.__dx *= -1

    def chang_dy_direction(self):
        # Setter
        self.__dy *= -1

    def remain_lives(self, count_lives, number_lives):
        ans = ''
        for i in range(number_lives-count_lives):
            ans += '❤'
        return ans
