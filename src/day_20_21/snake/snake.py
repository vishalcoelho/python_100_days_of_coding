from turtle import Turtle
from typing import List

MOVE_DISTANCE = 20

HEADING_UP = 90.0
HEADING_DOWN = 270.0
HEADING_LEFT = 180.0
HEADING_RIGHT = 0.0


class Snake:
    """Manages the snake's segments, movement, and direction in the Snake game."""

    segments: List[Turtle] = []
    update_delay: float = 0.1
    current_heading: float = 0.0

    def __init__(
        self,
        color: str = "white",
    ):
        """Initialise the snake with 3 segments laid horizontally at the centre.

        Args:
            color: Fill colour for all snake segments. Defaults to "white".
        """
        # snake starts off as a collection of 3 20x20 pixel turtles
        #        < 20>
        #      ^ +---+---+---+
        #     20 | . | . | . |
        #      v +-|-+-|-+-v-+
        #          |   v   at 0,0
        #          v   at -20,0
        #          at -40,0
        self.color = color
        self.segments = []
        STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
        for position in STARTING_POSITIONS:
            self._add_segment(position)

        self.head = self.segments[0]

    def move(self) -> None:
        """Advance the snake by one step.

        Shifts each segment into the position of the one ahead of it, moves
        the head forward by MOVE_DISTANCE pixels, then records the new heading
        in current_heading.
        """

        # Starting from the last segment of the snake, move each segment such that is occupies
        # the segment preceding it. For example, segment 3 moves into segment 2 positions,
        # segment 2 into 1, segment 1--the head of the snake--moves per the user's direction
        for seg_idx in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_idx - 1].xcor()
            new_y = self.segments[seg_idx - 1].ycor()
            self.segments[seg_idx].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)
        # update the snake's current heading
        self.current_heading = self.head.heading()

    def up(self) -> None:
        """Point the snake's head upward (north). Ignored if currently heading south."""
        if self.current_heading != HEADING_DOWN:
            self.head.setheading(HEADING_UP)

    def down(self) -> None:
        """Point the snake's head downward (south). Ignored if currently heading north."""
        if self.current_heading != HEADING_UP:
            self.head.setheading(HEADING_DOWN)

    def left(self) -> None:
        """Point the snake's head left (west). Ignored if currently heading right."""
        if self.current_heading != HEADING_RIGHT:
            self.head.setheading(HEADING_LEFT)

    def right(self) -> None:
        """Point the snake's head right (east). Ignored if currently heading left."""
        if self.current_heading != HEADING_LEFT:
            self.head.setheading(HEADING_RIGHT)

    def _add_segment(self, position) -> None:
        new_segment = Turtle("square")
        new_segment.color(self.color)
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def grow(self) -> None:
        self._add_segment(self.segments[-1].position())
