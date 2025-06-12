import curses

class Menu:
    def __init__(self, options):
        self.options = options
        self.selected = 0

    def navigate(self, direction):
        self.selected = (self.selected + direction) % len(self.options)

    def display(self, window):
        h, w = window.getmaxyx()
        for idx, option in enumerate(self.options):
            x = w//2 - len(option)//2
            y = h//2 - len(self.options)//2 + idx
            if idx == self.selected:
                window.attron(curses.A_REVERSE)
                window.addstr(y, x, option)
                window.attroff(curses.A_REVERSE)
            else:
                window.addstr(y, x, option)
        window.refresh()


def draw_square(win, top, left, size, color):
    for i in range(size):
        win.addch(top, left + i, ord('█'), curses.color_pair(color))
        win.addch(top + size - 1, left + i, ord('█'), curses.color_pair(color))
        win.addch(top + i, left, ord('█'), curses.color_pair(color))
        win.addch(top + i, left + size - 1, ord('█'), curses.color_pair(color))
    win.refresh()


def main(stdscr):
    curses.curs_set(0)
    curses.start_color()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    menu = Menu(["Draw Square", "Exit"])

    while True:
        stdscr.clear()
        menu.display(stdscr)
        key = stdscr.getch()
        if key == curses.KEY_UP:
            menu.navigate(-1)
        elif key == curses.KEY_DOWN:
            menu.navigate(1)
        elif key in (curses.KEY_ENTER, ord('\n')):
            if menu.selected == 0:
                stdscr.clear()
                h, w = stdscr.getmaxyx()
                size = min(h, w) // 4
                draw_square(stdscr, (h - size)//2, (w - size)//2, size, 1)
                stdscr.getch()
            else:
                break

curses.wrapper(main)
