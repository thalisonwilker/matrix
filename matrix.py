import time
import curses
import argparse

# Define the ASCII art of the white rabbit
white_rabbit_ascii = (
    """
                    (`.         ,-,
                    ` `.    ,;' /
                     `.  ,'/ .'
                      `. X /.'
            .-;--''--.._` ` (
          .'            /   `
         ,           ` '   Q '
         ,         ,   `._    \\
      ,.|         '     `-.;_'
      :  . `  ;    `  ` --,.._;
       ' `    ,   )   .'
          `._ ,  '   /_
             ; ,''-,;' ``-
              ``-..__``--`
""")


def animate_rabbit(stdscr, num_spaces_per_hop, num_repeats, rabbit_ascii):
    curses.curs_set(0)  # Hide the cursor
    for _ in range(num_repeats):
        for hop in range(5):  # Simulate a hopping motion
            # Split the ASCII art into lines
            white_rabbit_lines = rabbit_ascii.splitlines()

            # Calculate the height of the console window
            max_height, max_width = stdscr.getmaxyx()

            # Print the rabbit with spaces added for hopping
            for i, line in enumerate(white_rabbit_lines):
                # Calculate the vertical position to print the line
                y = i + 2 + hop  # Add 2 for some top margin and hop position
                if y < max_height:
                    # Add spaces to the beginning of each line to shift it to the right
                    spaced_line = ' ' * num_spaces_per_hop + line
                    stdscr.addstr(y, 0, spaced_line)
                    stdscr.refresh()

            # Add a delay between hops
            time.sleep(0.2)  # Adjust the delay duration as needed
            stdscr.clear()

        # Shift the rabbit one character to the right by adding a space to each line
        rabbit_ascii = '\n'.join(
            [' ' * num_spaces_per_hop + line for line in rabbit_ascii.splitlines()])
        stdscr.clear()


def main(stdscr, rabbit_only):
    stdscr.clear()
    if not rabbit_only:
        phrase = ['Wake up, Neo...', 'The matrix has you...',
                  'Follow the white rabbit...']
        for i in phrase:
            for c in i:
                if c == '.':
                    time.sleep(0.2)
                elif c == ' ':
                    time.sleep(0.3)
                else:
                    time.sleep(0.1)
                stdscr.addch(c)
                stdscr.refresh()
            stdscr.addch('\n')
            stdscr.refresh()
            time.sleep(0.7)

    stdscr.addstr(white_rabbit_ascii)
    stdscr.refresh()
    time.sleep(0.1)
    stdscr.addch('\n')
    stdscr.refresh()
    # Number of spaces to add for each hop
    num_spaces_per_hop = 8

    # Number of times to repeat the hopping animation
    num_repeats = 8

    # Call the function with the specified parameters and pass rabbit_ascii
    animate_rabbit(stdscr, num_spaces_per_hop,
                   num_repeats, white_rabbit_ascii)
    stdscr.clear()
    time.sleep(1.5)

    if not rabbit_only or (not 'phrase' and not phrase):
        stdscr.addstr('Knock, Knock, Neo.')
        stdscr.refresh()
        time.sleep(30)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Matrix Rabbit Animation')
    parser.add_argument('--rabbit-only', action='store_true',
                        help='Perform rabbit animation only')

    args = parser.parse_args()

    curses.wrapper(main, args.rabbit_only)
