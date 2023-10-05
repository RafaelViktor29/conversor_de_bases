import customtkinter as ctk
import pyperclip

from conversor import Conversor

c = Conversor()

bases = ('Bin', 'Oct', 'Dec', 'Hex')
bases_complete = ('Binário', 'Octal', 'Decimal', 'Hexadecimal')


def update_results():
    input_text = entry.get()
    base = radio_var.get()

    if input_text:
        outputs[0].configure(text=c.to_binary(input_text, base))
        outputs[1].configure(text=c.to_octal(input_text, base))
        outputs[2].configure(text=c.to_decimal(input_text, base))
        outputs[3].configure(text=c.to_hexadecimal(input_text, base))
    else:
        for i in range(4):
            outputs[i].configure(text='')


def update_results_and_display():
    update_results()


def copy_output(index):
    input_text = outputs[index].cget('text')
    pyperclip.copy(input_text)

    outputs[index].configure(text_color='#44E01D')
    root.after(500, lambda: outputs[index].configure(text_color='#FFFFFF'))


def update_radio_var(base, value):
    radio_var.set(base)
    on_radio_select(value)


def validate_char(input_text, base_index):
    bases_chars = ('01', '01234567', '0123456789', '0123456789abcdefABCDEF')
    valid_chars = set(bases_chars[base_index])
    return all(char in valid_chars for char in input_text)


def on_radio_select(value):
    entry_label.configure(text=value)
    entry.delete(0, ctk.END)
    update_results()
    update_button_state()

    for i, radio in enumerate(radios):
        if value == bases_complete[i]:
            radio.configure(text_color='#00DCFF')
        else:
            radio.configure(text_color='#FFFFFF')

    if value == 'Binário':
        entry.configure(validate='key', validatecommand=(
            root.register(lambda P: validate_char(P, 0)), '%P'))
    elif value == 'Octal':
        entry.configure(validate='key', validatecommand=(
            root.register(lambda P: validate_char(P, 1)), '%P'))
    elif value == 'Decimal':
        entry.configure(validate='key', validatecommand=(
            root.register(lambda P: validate_char(P, 2)), '%P'))
    else:
        entry.configure(validate='key', validatecommand=(
            root.register(lambda P: validate_char(P, 3)), '%P'))


def press(key):
    current_text = entry.get()
    if key == 'c':
        entry.delete(0, ctk.END)
    elif key == '<':
        current_text = current_text[:-1]
        entry.delete(0, ctk.END)
        entry.insert(ctk.END, current_text)
    else:
        entry.insert(ctk.END, key)

    update_results_and_display()


root = ctk.CTk()
root.geometry('500x650')
root.resizable(False, False)
root.title('Conversor de bases')

entry_frame = ctk.CTkFrame(root)
entry_frame.pack(pady=[10, 0], padx=10)

entry_label = ctk.CTkLabel(
    text='Decimal',
    master=entry_frame,
    font=('Fira Code', 18)
)
entry_label.pack(padx=20, anchor='e')

entry = ctk.CTkEntry(
    master=entry_frame,
    font=('Fira Code', 28),
    width=440,
    height=50
)
entry.pack(pady=[0, 10], padx=10, anchor='w')

entry.bind('<KeyRelease>', lambda event: update_results())
entry.configure(validate='key', validatecommand=(root.register(
    lambda P: validate_char(P, 2)), '%P'))

frame = ctk.CTkFrame(root, width=440)
frame.pack(pady=[10, 0], padx=20)

radio_var = ctk.StringVar()
radio_var.set('Dec')
radio_frame = ctk.CTkFrame(frame)
radio_frame.pack(pady=10, padx=10, side='left')

radios = []
for i, base in enumerate(bases):
    color = '#00DCFF' if base == 'Dec' else '#FFFFFF'
    top = 7.5 if base != 'Bin' else 10
    bot = 7.5 if base != 'Hex' else 10

    radio = ctk.CTkRadioButton(
        master=radio_frame,
        text=base,
        variable=radio_var,
        value=base,
        font=('Fira Code', 20),
        command=lambda value=bases_complete[i]: on_radio_select(value),
        border_width_unchecked=0,
        border_width_checked=0,
        text_color=color
    )
    radio.pack(pady=[top, bot], padx=0)
    radios.append(radio)

output_frame = ctk.CTkFrame(frame)
output_frame.pack(pady=10, padx=10, side='right')

outputs = []
for base in bases:
    top = 5 if base != 'Bin' else 10
    bot = 5 if base != 'Hex' else 10

    output = ctk.CTkLabel(
        master=output_frame,
        font=('Fira Code', 20),
        text='',
        text_color='#FFFFFF',
        width=400,
        anchor='w',
        justify='left'
    )
    output.pack(pady=[top, bot], padx=10)
    outputs.append(output)

outputs[0].bind('<Button-1>', lambda x: copy_output(0))
outputs[1].bind('<Button-1>', lambda x: copy_output(1))
outputs[2].bind('<Button-1>', lambda x: copy_output(2))
outputs[3].bind('<Button-1>', lambda x: copy_output(3))

button_frame = ctk.CTkFrame(root)
button_frame.pack(pady=10, padx=20, fill='both', expand=True)
alfa_frame = ctk.CTkFrame(button_frame, width=100, fg_color='#2B2B2B')
alfa_frame.pack(pady=20, padx=10, fill='y', side='left')

alfas = []
for i, alfa in enumerate('ABCDEF'):
    bot = 0 if alfa != 'F' else 5

    alfa_button = ctk.CTkButton(
        master=alfa_frame, text=alfa, height=42.33,
        fg_color='#2B2B2B', font=('Fira Code', 22),
        command=lambda key=alfa: press(key),
        text_color_disabled='#515151', state='disabled'
    )
    alfa_button.grid(pady=[5, bot], row=i, column=0)
    alfas.append(alfa_button)

num_frame = ctk.CTkFrame(button_frame, width=400,
                         height=400, fg_color='#2B2B2B')
num_frame.pack(pady=20, padx=10, fill='y', side='left')

buttons = []
for col, button_group in enumerate(['741c', '8520', '963<']):
    for row, string in enumerate(button_group):
        bot = 5 if string in 'c0<' else 0
        x = 6 if col == 1 else 0
        fg = '#333333' if string not in 'c<' else '#404040'

        if string == 'c':
            str_text = 'ce'
        elif string == '<':
            str_text = ' ⌫ '
        else:
            str_text = string

        button = ctk.CTkButton(
            master=num_frame, text=str_text, height=66, width=88,
            fg_color=fg, font=('Fira Code', 22),
            text_color_disabled='#515151',
            command=lambda key=string: press(key)
        )
        button.grid(pady=[5, bot], padx=x, row=row, column=col)
        buttons.append(button)


def clear_entry(event):
    entry.delete(0, ctk.END)


root.bind("<Escape>", clear_entry)


def disable_buttons(index_base):
    buttons_base = ('01', '01234567', '0123456789', '0123456789')

    for i, num in enumerate('741c8520962<'):
        if num in 'c<':
            continue

        stt = 'normal' if num in buttons_base[index_base] else 'disabled'
        fg = '#333333' if stt == 'normal' else '#2B2B2B'
        color = '#FFFFFF' if stt == 'normal' else '#333333'

        buttons[i].configure(state=stt, fg_color=fg, text_color=color)

    for i in range(6):
        stt_alfa = 'normal' if index_base == 3 else 'disabled'
        fg = '#333333' if stt_alfa == 'normal' else '#2B2B2B'
        color = '#FFFFFF' if stt_alfa == 'normal' else '#333333'

        alfas[i].configure(state=stt_alfa, fg_color=fg, text_color=color)


def update_button_state():
    selected_base = radio_var.get()

    if selected_base == bases[0]:
        disable_buttons(0)
    elif selected_base == bases[1]:
        disable_buttons(1)
    elif selected_base == bases[2]:
        disable_buttons(2)
    else:
        disable_buttons(3)


if __name__ == '__main__':
    root.mainloop()
