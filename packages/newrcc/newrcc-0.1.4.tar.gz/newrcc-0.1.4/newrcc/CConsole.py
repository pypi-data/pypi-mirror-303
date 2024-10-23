from newrcc import CError as ce
from newrcc import CColor as cc


def colorfulText(text: str,
                 color: None | str | cc.Color | tuple[cc.TextColor | tuple[int, int, int],
                                                      cc.BackgroundColor | tuple[int, int, int]],
                 reset: bool = True, decorations: list[cc.Decoration | str] = None) -> str:
    if decorations is not None:
        for decoration in decorations:
            if isinstance(decoration, str):
                text = decoration + text
            else:
                text = str(decoration) + text
    if isinstance(color, cc.Color):
        text = str(color) + text
    elif isinstance(color, tuple):
        if isinstance(color[0], tuple):
            text = str(cc.TextColor(color[0])) + text
        else:
            text = str(color[0]) + text
        if isinstance(color[1], tuple):
            text = str(cc.BackgroundColor(color[1])) + text
        else:
            text = str(color[1]) + text
    elif isinstance(color, str):
        text = color + text
    elif color is not None:
        raise cc.CDError.CDUnexpectedColorInputError(color, 'colorfulText')
    if reset and color is not None:
        text += cc.Reset
    return text


def colorfulPrint(text: str, color: str | cc.Color | tuple[
    cc.TextColor | str | tuple[int, int, int], cc.BackgroundColor | str | tuple[int, int, int]], reset: bool = True,
                  end: str = '\n',
                  decorations: list[cc.Decoration | str] = None) -> None:
    text = colorfulText(text, color, reset, decorations)
    print(text, end=end)


class ProcessBar:
    def __init__(self, prefix: str, suffix: str, total: int, length: int = 20,
                 title_color: str | cc.Color = None, frame_color: str | cc.Color = None,
                 show_frame_border: bool = True,
                 process_color: str | cc.Color = None, value_color: str | cc.Color = None):
        self.prefix = prefix
        self.suffix = suffix
        self.length = length
        self.total = total
        self.process_color = process_color
        self.frame_color = frame_color
        self.show_frame_border = show_frame_border
        self.title_color = title_color
        self.value_color = value_color
        self.extra_length = (8 * (process_color is not None) + 8 * (frame_color is not None) +
                             8 * (title_color is not None) + 12 * (value_color is not None))
        self.process_length = self.extra_length

    def draw(self, current: int, style: int = 1) -> None:
        real_length = int(self.length * current // self.total)
        fix_length = max(len(self.prefix), len(self.suffix))

        def getProcess():
            _process = ''
            if style == 1:
                _process = (colorfulText('│' * self.show_frame_border, self.frame_color, reset=False) +
                            colorfulText('█' * real_length + ' ' * (self.length - real_length), self.process_color) +
                            colorfulText('│' * self.show_frame_border, self.frame_color))
            elif style == 2:
                _process = (colorfulText('│' * self.show_frame_border, self.frame_color, reset=False) +
                            colorfulText('█' * real_length, self.process_color) +
                            colorfulText('█' * (self.length - real_length), self.frame_color) +
                            colorfulText('│' * self.show_frame_border, self.frame_color))
            elif style == 3:
                _process = (colorfulText('│' * self.show_frame_border, self.frame_color, reset=False) +
                            colorfulText('━' * (real_length - 1), self.process_color, reset=False) +
                            '╸' * (self.length - real_length > 0) +
                            '━' * (self.length - real_length == 0) + cc.Reset +
                            colorfulText('━' * (self.length - real_length), self.frame_color, reset=False) +
                            colorfulText('│' * self.show_frame_border, self.frame_color))
            return _process

        if real_length < self.length:
            process = (colorfulText(self.prefix + ' ' * (fix_length - len(self.prefix)), self.title_color) +
                       ': ' +
                       getProcess() +
                       ' ' +
                       colorfulText(str(round(current / self.total * 100, 3)) + '% ', self.value_color))
            print(process, end='')
            self.process_length = len(process)
        else:
            process = (colorfulText(self.suffix + ' ' * (fix_length - len(self.suffix)), self.title_color) +
                       ': ' +
                       getProcess() +
                       ' ' +
                       colorfulText(str(round(current / self.total * 100, 3)) + '% ', self.value_color))
            print(process)

    def erase(self) -> None:
        print('\b' * (self.process_length + self.extra_length), end='', flush=True)


class TBlock:
    def __init__(self, item, across_rows: int = 1, across_columns: int = 1, isnone: bool = False):
        self.item = str(item)
        self.across_rows = across_rows
        self.across_columns = across_columns
        self.row_across = (across_rows != 1)
        self.column_across = (across_columns != 1)
        self.isnone = isnone

    def __str__(self):
        if self.isnone:
            return "<none>"
        else:
            return self.item


class TRow:
    def __init__(self, blocks: list[TBlock]):
        self.blocks = []
        for block in blocks:
            if block.column_across:
                self.blocks.append(block)
                i = 1
                for _ in range(0, block.across_columns - 1):
                    self.blocks.append(TBlock('', across_columns=block.across_columns - i, isnone=True))
                    i += 1
            else:
                self.blocks.append(block)
        length = 0
        across_rows = 0
        for block in blocks:
            length += block.across_columns
            across_rows = max(across_rows, block.across_rows)
        block_length = []
        for block in blocks:
            block_length.append(len(str(block)))
            if block.across_columns > 1:
                for i in range(0, block.across_columns - 1):
                    block_length.append(0)
        self.columns = length
        self.across_rows = across_rows
        self.block_length = block_length

    def __blocks_str__(self):
        string = '[ '
        for block in self.blocks:
            string += str(block) + ' '
        string += ']'
        return string

    def __str__(self):
        return f'row{'{'}across rows: {self.across_rows}, columns: {self.columns}, block length: {self.block_length}, blocks: {self.__blocks_str__()}{'}'}'


class Table:
    def getBlockMaxLength(self):
        block_max_length = [0 for _ in self.rows[0].block_length]
        for _row in self.rows:
            if len(block_max_length) != len(_row.block_length):
                raise ce.CDTableBlockCountMismatchedError(_row, block_max_length)
            i = 0
            for length in _row.block_length:
                block_max_length[i] = max(length, block_max_length[i])
                i += 1
        return block_max_length

    def __init__(self, rows: list[TRow] = None):
        self.rows = rows
        row_length = 0
        column_length = 0
        for row in rows:
            row_length += row.across_rows
            column_length = max(column_length, row.columns)
        self.row_length = row_length
        self.column_length = column_length
        self.block_max_length = self.getBlockMaxLength()

    def append(self, row: TRow):
        self.rows.append(row)

    def getTableInfo(self):
        return (f'table{'{'}row_length: {self.row_length}, column_length: {self.column_length},' +
                f' block max length: {self.block_max_length}{'}'}')

    def __str__(self):
        r_index = 0
        while r_index < self.row_length:
            if r_index == 0:
                print(end='┌')
                length_index = 0
                while length_index < len(self.block_max_length):
                    print(end='─' * self.block_max_length[length_index])
                    if length_index == len(self.block_max_length) - 1:
                        print(end='┐\n')
                    else:
                        if self.rows[r_index].blocks[length_index].column_across:
                            print(end='─')
                        else:
                            print(end='┬')
                    length_index += 1
                block_index = 0
                for block in self.rows[r_index].blocks:
                    if not block.isnone:
                        print(end='│' + str(block) + ' ' * (self.block_max_length[block_index] - len(str(block))))
                    else:
                        print(end=' ' * (self.block_max_length[block_index] + 1))
                    block_index += 1
                print(end='│\n')
            else:
                print(end='├')
                length_index = 0
                while length_index < len(self.block_max_length):
                    print(end='─' * self.block_max_length[length_index])
                    if length_index == len(self.block_max_length) - 1:
                        print(end='┤\n')
                    else:
                        if not self.rows[r_index].blocks[length_index].column_across and not \
                                self.rows[r_index - 1].blocks[length_index].column_across:
                            print(end='┼')
                        elif not self.rows[r_index].blocks[length_index].column_across and \
                                self.rows[r_index - 1].blocks[length_index].column_across:
                            print(end='┬')
                        elif self.rows[r_index].blocks[length_index].column_across and self.rows[r_index - 1].blocks[
                            length_index].column_across:
                            print(end='─')
                        elif self.rows[r_index].blocks[length_index].column_across and not \
                                self.rows[r_index - 1].blocks[length_index].column_across:
                            print(end='┴')
                    length_index += 1
                block_index = 0
                for block in self.rows[r_index].blocks:
                    if not block.isnone:
                        print(end='│' + str(block) + ' ' * (self.block_max_length[block_index] - len(str(block))))
                    else:
                        print(end=' ' * (self.block_max_length[block_index] + 1))
                    block_index += 1
                print(end='│\n')
            r_index += 1
        length_index = 0
        print(end='└')
        while length_index < len(self.block_max_length):
            print(end='─' * self.block_max_length[length_index])
            if length_index == len(self.block_max_length) - 1:
                print(end='┘\n')
            else:
                if self.rows[r_index - 1].blocks[length_index].column_across:
                    print(end='─')
                else:
                    print(end='┴')
            length_index += 1
        return ''


"""
─ │ ┌ ┐ └ ┘ ┼ ├ ┤ ┬ ┴ █ ▓ ▒ ░ ↑ ↓ ← → ● ◦ ․·‥°º▫◌◯◻⁺ⁱ⁼∙⋱﹒·−-⁎‣−■■■■■■■■■■■■■ ━ ━ ╺ ╸
"""

# # Processing bar
# process_bar = ProcessBar(colorfulText('test', cdc.TextColor.CYAN),
#                          colorfulText('finish', cdc.TextColor.BLUE),
#                          100, 50,frame_color=cdc.TextColor(cdc.TextColor.CYAN),
#                          show_frame_border=False, process_color=cdc.TextColor((225, 0, 0)),
#                          value_color=cdc.TextColor(cdc.TextColor.GREEN))
# for i in range(1, 101):
#     process_bar.draw(i, style=3)
#     time.sleep(0.05)
#     process_bar.erase()

# blocks1 = [TBlock(123), TBlock(234, across_columns=3), TBlock(456)]
# blocks2 = [TBlock(234), TBlock(345), TBlock(567), TBlock('what is this', across_columns=2)]
# blocks3 = [TBlock(987), TBlock(375, across_columns=2), TBlock('hello'), TBlock('world')]
#
# rows = [TRow(blocks1), TRow(blocks2), TRow(blocks3)]

# for row in rows:
#     print(row)

# table = Table(rows)
#
# print(table)
