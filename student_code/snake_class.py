"""
This module includes class Snake and class BuildSnake for the main game which is called Snake game.
"""
class Snake():
    """
    Snake class is a structure for game snake which needs some attributes and methodes to initialize
     and execute the game.

    Attributes:
    -----------------
        snake_head_position : tuple(int, int)
            (tuple with x- and y-values)
            Starting position of the head.
            The top-left part of the block representing the head's coordinates of the snake.

        snake_size : tuple(int, int)
            Blocks' size which are to build up the snake (tuple with width and height).

        colour : tuple(int, int, int)
            (tuple with colour values (r,g,b))
            The colour of blocks that are to build up the snake.

        grow_object : Callable
            An object which calls BuildSnake class.
            Saved for access to new coordinates used to call BuildSnake on the
             BuildSnake-attribute.

        seq : list
            An attribute which includes coordinates, size and colour of snake's body blocks.
            This is empty at the first step since snake has just head block without body
             block.

        index : int
            This is index which used in iter function of Snake class and it is empty
             at the first step.

    Methods:
    -----------------
        move_left():
            Function to move left the head and body blocks of snake.

        move_right():
            Function to move right the head and body blocks of snake.
            The game has been set from this type of movement.

        move_up():
            Function to move up the head and body blocks of snake.

        move_down():
            Function to move down the head and body blocks of snake.

        inside_bounds(screen_top_left, screen_bottom_right):
            Function Used to control whether the snake is inside the boundaries of
            the screen or not. If the snake is not inside the boundaries,the game
            is over. The function takes two arguments, top left and bottom right
            coordinates of the bound and they are in order it returns bool
            "True or False". The snake is inside the given bounds if the right
            side of the snake coincide with the right side of the given bounds.

        check_collision(fruit_coordinates, fruit_size):
            The function used to check collision during the game while fruit
            will make and move, any collisions should not be appear with any
            blocks of snake's head and body. The function takes two tuple value
            which are top left coordinates of the shape and the width and height
            of it, respectively. The function will return true if any of the
            body-parts of the snake collide, otherwise false.

        check_collision_with_fruit(fruit_coordinates, fruit_size):
            The function used to check collision with fruit during the game while
            snake take fruit if the head of the snake completely overlaps with
            the fruit collision will happen.The function takes two tuple value
            which are the top left coordinates of the shape and the width and height
            of it, respectively. The function will return true if the head of the snake
            completely overlaps with the fruit, otherwise false.

        check_collision_with_self():
            The function used to check collision of the head of snake with
            each blocks of snake's body. There is clear that the head will not have a
            collid with the second block of snake.The function will return true if the
            snake collide with itself, otherwise false.

        grow():
            Function which add all parts of snake body via coordinates which available in
            BuildSnake class.

        iter():
            The function is an iterator which return attributes of each part of snake to snake_game
            and after that via snake_game, get_coordinates and get_size and so get_colour
            from BuildSnake class will call for drawing the new block of snake body and other
            related implementations.
    """

    def __init__(self, start_position, snake_size, colour):
        """Initialize the class. The parameters are passed on to the init function BuildSnake
           class

        Parameters:
        ------------------------------------------
        start_position : tuple(int, int)
            The x- and y-values for starting position of the snake head.

        snake_size : tuple(int, int)
            Snake blocks' size with width and heigh those are to build up the snake.

        colour : tuple(int, int)
            Colour of the blocks that are to build up the snake with colour values r,g,b.
        """
        self.snake_head_position = list(start_position)
        self.snake_size = list(snake_size)
        self.colour = colour
        self.grow_object = BuildSnake(self.snake_head_position, self.snake_size, self.colour)
        self.seq = []
        self.seq.append(self.grow_object)
        self._index = 0

    def move_left(self):
        """Moves the head one block-length in left direction.

        The rest of the body must follow the head, but cannot always be directly moved
        in the desired direction
        """

        new_coordinate = self.seq[0].get_coordinates()
        new_coordinate_x = new_coordinate[0]
        new_coordinate_y = new_coordinate[1]
        self.snake_head_position[0] = self.snake_head_position[0] - self.snake_size[0]
        if len(self.seq) > 1:
            for i in range(1, len(self.seq)):
                if len(self.seq)-i != 1:
                    move_body_coordinate = self.seq[len(self.seq)-i-1].get_coordinates()
                    move_body_coordinate_xx = move_body_coordinate[0]
                    move_body_coordinate_yy = move_body_coordinate[1]
                    (self.seq[len(self.seq)-i].set_coordinates
                     ([move_body_coordinate_xx, move_body_coordinate_yy]))
                else:
                    self.seq[1].set_coordinates([new_coordinate_x, new_coordinate_y])

    def move_right(self):
        """Moves the head one block-length in right direction.

        The rest of the body must follow the head, but cannot always be directly moved
        in the desired direction
        """

        new_coordinate = self.seq[0].get_coordinates()
        new_coordinate_x = new_coordinate[0]
        new_coordinate_y = new_coordinate[1]
        self.snake_head_position[0] = self.snake_head_position[0] + self.snake_size[0]
        if len(self.seq) > 1:
            for i in range(1, len(self.seq)):
                if len(self.seq)-i != 1:
                    move_body_coordinate = self.seq[len(self.seq)-i-1].get_coordinates()
                    move_body_coordinate_xx = move_body_coordinate[0]
                    move_body_coordinate_yy = move_body_coordinate[1]
                    (self.seq[len(self.seq)-i].set_coordinates
                     ([move_body_coordinate_xx, move_body_coordinate_yy]))
                else:
                    self.seq[1].set_coordinates([new_coordinate_x, new_coordinate_y])

    def move_up(self):
        """Moves the head one block-length in up direction.

        The default movement of snake is move_up at the start of the game.

        The rest of the body must follow the head, but cannot always be directly moved
        in the desired direction
        """

        new_coordinate = self.seq[0].get_coordinates()
        new_coordinate_x = new_coordinate[0]
        new_coordinate_y = new_coordinate[1]
        self.snake_head_position[1] = self.snake_head_position[1] - self.snake_size[1]
        if len(self.seq) > 1:
            for i in range(1, len(self.seq)):
                if len(self.seq)-i != 1:
                    move_body_coordinate = self.seq[len(self.seq)-i-1].get_coordinates()
                    move_body_coordinate_xx = move_body_coordinate[0]
                    move_body_coordinate_yy = move_body_coordinate[1]
                    (self.seq[len(self.seq)-i].set_coordinates
                     ([move_body_coordinate_xx, move_body_coordinate_yy]))
                else:
                    self.seq[1].set_coordinates([new_coordinate_x, new_coordinate_y])

    def move_down(self):
        """Moves the head one block-length in down direction.

        The rest of the body must follow the head, but cannot always be directly moved
        in the desired direction
        """

        new_coordinate = self.seq[0].get_coordinates()
        new_coordinate_x = new_coordinate[0]
        new_coordinate_y = new_coordinate[1]
        self.snake_head_position[1] = self.snake_head_position[1] + self.snake_size[1]
        if len(self.seq) > 1:
            for i in range(1, len(self.seq)):
                if len(self.seq)-i != 1:
                    move_body_coordinate = self.seq[len(self.seq)-i-1].get_coordinates()
                    move_body_coordinate_xx = move_body_coordinate[0]
                    move_body_coordinate_yy = move_body_coordinate[1]
                    (self.seq[len(self.seq)-i].set_coordinates
                     ([move_body_coordinate_xx, move_body_coordinate_yy]))
                else:
                    self.seq[1].set_coordinates([new_coordinate_x, new_coordinate_y])

    def inside_bounds(self, screen_top_left, screen_bottom_right):
        """
        Used to control whether the snake is inside the boundaries of the screen
        or not.

        The snake is inside the given bounds if the right side of the snake coincide with
        the right side of the given bounds.
        """

        screen_top_left = list(screen_top_left)
        screen_bottom_right = list(screen_bottom_right)
        if  (self.snake_head_position[0] <= (screen_bottom_right[0] - self.snake_size[0]) and
             self.snake_head_position[1] <= (screen_bottom_right[1] - self.snake_size[1])):
            if screen_top_left[0] <= self.snake_head_position[0] <= screen_bottom_right[0]:
                if screen_top_left[1] <= self.snake_head_position[1] <= screen_bottom_right[1]:
                    if  self.snake_size[0] <= screen_bottom_right[0] - screen_top_left[0]:
                        if  self.snake_size[1] <= screen_bottom_right[1] - screen_top_left[1]:
                            return True
        return False

    def check_collision(self, fruit_coordinates, fruit_size):
        """The function checks if any body-parts of the snake collide with fruits which
        randomly made.

        The function should detect it does not collide with the snake anymore.
        Parameters:
            fruit_coordinates
                top left coordinates of the shape to check collision with snake

            fruit_size
                the width and height of the shape to check collision with snake
        """

        self.fruit_size = fruit_size
        for part in self.seq:
            if fruit_coordinates == part.get_coordinates():
                return True
        return False

    def check_collision_with_fruit(self, fruit_coordinates, fruit_size):
        """The function checks if the head of the snake completely overlaps with the fruit.

        Parameters:
            fruit_coordinates
                top left coordinates of the shape to check collision with snake

            fruit_size
                the width and height of the shape to check collision with snake
        """

        self.fruit_size = fruit_size
        if (self.snake_head_position[0] == fruit_coordinates[0] and
                self.snake_head_position[1] == fruit_coordinates[1]):
            return True
        return False

    def check_collision_with_self(self):
        """The function used to check collision of the head of snake with each blocks of
        snake's body.
        """

        for i in range(0, len(self.seq)-1):
            if self.seq[0].coordinates == self.seq[i+1].coordinates:
                return True
        return False

    def grow(self):
        """add all parts of snake body via coordinates which available in BuildSnake class.
        """

        self.grow_object = BuildSnake(self.seq[-1].coordinates, self.snake_size, self.colour)
        self.seq.append(self.grow_object)

    def __iter__(self):
        """It makes all parts of Snake class iterable and useable."""

        return self

    def __len__(self):
        return len(self.seq)

    def __next__(self):
        if len(self) == self._index:
            self._index = 0
            raise StopIteration
        self._index += 1
        return self.seq[self._index-1]

class BuildSnake():
    """Get coordinates, size and colour as attributes and Set the new ones.

     The blocks building up the snake is created in a separate class named BuildSnake.

    Attributes:
     -----------------
        self.coordinates = coordinates
         It includes the x- and y-coordinates of the snake block as a tuple

        self.size = size
         It includes the width and height of the snake block a tuple

        self.colour = colour
         It includes the colour of the snake block as a tuple (r, g, b)

    Methodes
     ------------------
        get_coordinates()
            get coordinates of snake parts and returnes the value whenever called

        set_coordinates()
            set new coordinates of snake parts and return the value whenever called

        get_size()
            get size of snake parts and returnes the value whenever called

        set_size()
            set new size of snake parts and return the value whenever called

        get_colour()
            get colour of snake parts and returnes the value whenever called

        set_colour()
            set new colour of snake parts and return the value whenever called
    """

    def __init__(self, coordinates, size, colour):
        """The function initialize coordinates, size and colour of each parts of snake.

        get_coordinates()
            Return the x- and y-coordinates as a tuple
        get_size()
            Return the width and height as a tuple
        get_colour()
            Return the colour of the block as a tuple (r, g, b)
        """

        self.coordinates = coordinates
        self.size = size
        self.colour = colour

    def get_coordinates(self):
        """The function get coordinates of snake parts and return the value whenever called."""

        return tuple(self.coordinates)

    def set_coordinates(self, coordinates):
        """The function set new coordinates of snake parts and return the value whenever called."""

        self.coordinates = coordinates

    def get_size(self):
        """The function get size of snake parts and return the value whenever called."""
        return tuple(self.size)

    def set_size(self, size):
        """The function set new coordinates of snake parts and return the value whenever called.

        This function would be used in the next developed phase of snake game
        """

        pass

    def get_colour(self):
        """The function get colour of snake parts and return the value whenever called."""

        return tuple(self.colour)

    def set_colour(self, colour):
        """The function set new coordinates of snake parts and return the value whenever called.

        This function would be used in the next developed phase of snake game
        """

        pass
