import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
import re
import os

version = '24.10.22'

root = None

def annotate_file():
    global root
    filepath = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if filepath:
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()
        root.destroy()
        content = content.replace('\n', ' \n')  # Add a space at the end of each line
        editor_interface(content, filepath)

def editor_interface(content, filepath):
    main_win = tk.Tk()
    main_win.title(f"Annotate File - {os.path.basename(filepath)}")

    last_selected_rcv = [None]
    rcv_tags = {}
    rcv_numbers = re.findall(r'\[.*?(?:Roll\s*No\.?|Rollcall\s*Vote\s*No\.).*?(\d+).*?\]', content, flags=re.IGNORECASE)
    for rcv in rcv_numbers:
        rcv_tags[rcv] = set()

    # Left Frame for Text Widget
    text_widget = tk.Text(main_win, wrap=tk.WORD)
    text_widget.insert(tk.END, content)
    text_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Right Frame for Controls
    right_frame = tk.Frame(main_win)
    right_frame.pack(side=tk.RIGHT, fill=tk.Y)

    # Roll Call Vote Frame
    rcv_frame = tk.LabelFrame(right_frame, text="Roll Call Vote")
    rcv_frame.pack(pady=5)

    rcv_listbox = tk.Listbox(rcv_frame)
    for rcv in rcv_tags:
        rcv_listbox.insert(tk.END, rcv)
    rcv_listbox.pack(pady=5)

    def add_rcv():
        rcv_num = simpledialog.askstring("Add RCV", "Enter Roll Call Vote number:")
        if rcv_num:
            if rcv_num not in rcv_tags:
                rcv_tags[rcv_num] = set()
                rcv_listbox.insert(tk.END, rcv_num)
            else:
                messagebox.showinfo("Duplicate RCV", "This RCV number already exists.")

    def select_rcv():
        selection = rcv_listbox.curselection()
        if not selection:
            messagebox.showwarning("No Selection", "Please select an RCV from the list.")
            return
        selected_rcv = rcv_listbox.get(selection[0])
        last_selected_rcv[0] = selected_rcv

        # Jump to the RCV in the text
        start_index, end_index = find_rcv(selected_rcv)
        if start_index:
            text_widget.see(start_index)

        if 'rcv' not in rcv_tags[selected_rcv]:
            add_tag('rcv', selected_rcv)

    def clear_tags():
        if not last_selected_rcv[0]:
            messagebox.showwarning("No RCV Selected", "Please select an RCV to clear tags.")
            return
        selected_rcv = last_selected_rcv[0]
        content = text_widget.get("1.0", tk.END)
        tag_pattern = rf'<.*? {selected_rcv}>|<\\.*? {selected_rcv}>'
        new_content = re.sub(tag_pattern, '', content)
        text_widget.delete("1.0", tk.END)
        text_widget.insert(tk.END, new_content)
        # Remove all tags related to the selected RCV
        for tag in text_widget.tag_names():
            if selected_rcv in tag:
                text_widget.tag_remove(tag, '1.0', tk.END)
        rcv_tags[selected_rcv].clear()
        select_rcv()

    tk.Button(rcv_frame, text="Add", command=add_rcv).pack(side=tk.LEFT, padx=5)
    tk.Button(rcv_frame, text="Select", command=select_rcv).pack(side=tk.LEFT, padx=5)
    tk.Button(rcv_frame, text="Clear Tags", command=clear_tags).pack(side=tk.LEFT, padx=5)

    # Mentions Frame
    mentions_frame = tk.LabelFrame(right_frame, text="Mentions")
    mentions_frame.pack(pady=5)

    def scan_mentions(patterns):
        # Scan the text for patterns
        content = text_widget.get("1.0", tk.END)
        mentions_count = {}
        for pattern in patterns:
            matches = re.findall(pattern, content, flags=re.IGNORECASE)
            for match in matches:
                standard_case = f"{match[0].upper()} {match[1]}"
                if standard_case in mentions_count:
                    mentions_count[standard_case] += 1
                else:
                    mentions_count[standard_case] = 1
        # Sort mentions by type and number
        sorted_mentions = sorted(mentions_count.items(), key=lambda x: (x[0].split()[0], int(re.findall(r'\d+', x[0])[0])))
        return sorted_mentions

    def show_mentions(mentions):
        if not mentions:
            messagebox.showinfo("No Mentions Found", "No mentions found in the text.")
            return
        def on_select(event):
            selection = mentions_listbox.curselection()
            if selection:
                selected_mention = mentions_listbox.get(selection[0]).split(' (')[0]  # Extract mention without count
                find_entry.delete(0, tk.END)
                find_entry.insert(0, selected_mention)
                find_text()
                mentions_win.destroy()

        mentions_win = tk.Toplevel(main_win)
        mentions_win.title("Mentions")

        mentions_listbox = tk.Listbox(mentions_win, width=30)
        for mention, count in mentions:
            mentions_listbox.insert(tk.END, f"{mention} ({count})")  # Display mention with count
        mentions_listbox.pack(padx=10, pady=10)
        mentions_listbox.bind('<<ListboxSelect>>', on_select)

        tk.Button(mentions_win, text="Cancel", command=mentions_win.destroy).pack(pady=5)

    def measure_button():
        measure_patterns = [
            r'\b(H\.R\.|S\.|H\. Res\.|S\. Res\.|H\. Con\. Res\.|H\.J\. Res\.|S\. Con\. Res\.|S\.J\. Res\.)\s*(\d{1,4})\b'
        ]
        mentions = scan_mentions(measure_patterns)
        show_mentions(mentions)

    def amendment_button():
        amendment_patterns = [
            r'\b(Amendment No\.|Amdt\. No\.)\s*(\d{1,4})\b'
        ]
        mentions = scan_mentions(amendment_patterns)
        show_mentions(mentions)

    tk.Button(mentions_frame, text="Measure", width=10, command=measure_button).pack(side=tk.LEFT, padx=5)
    tk.Button(mentions_frame, text="Amendment", width=10, command=amendment_button).pack(side=tk.LEFT, padx=5)

    # Search Section
    search_vars = {'matches': [], 'current_match': 0}

    def find_text():
        search_text = find_entry.get()
        if not search_text:
            messagebox.showwarning("No Search Text", "Please enter text to search.")
            return
        text_widget.tag_remove('search_highlight', '1.0', tk.END)
        search_vars['matches'] = []
        search_vars['current_match'] = 0
        start_pos = '1.0'
        while True:
            idx = text_widget.search(search_text, start_pos, stopindex=tk.END, nocase=1)
            if not idx:
                break
            end_idx = f"{idx}+{len(search_text)}c"
            text_widget.tag_add('search_highlight', idx, end_idx)
            search_vars['matches'].append((idx, end_idx))
            start_pos = end_idx
        text_widget.tag_config('search_highlight', background='yellow')
        num_matches = len(search_vars['matches'])
        if num_matches == 0:
            messagebox.showinfo("No Matches", f"No matches found for '{search_text}'.")
            next_button.config(state=tk.DISABLED, text="Next")
        else:
            idx, _ = search_vars['matches'][0]
            text_widget.mark_set(tk.INSERT, idx)
            text_widget.see(idx)
            update_next_button_label()
            next_button.config(state=tk.NORMAL if num_matches > 1 else tk.DISABLED)

    def find_next():
        num_matches = len(search_vars['matches'])
        if num_matches <= 1:
            return
        search_vars['current_match'] = (search_vars['current_match'] + 1) % num_matches
        idx, _ = search_vars['matches'][search_vars['current_match']]
        text_widget.mark_set(tk.INSERT, idx)
        text_widget.see(idx)
        update_next_button_label()

    def update_next_button_label():
        current = search_vars['current_match'] + 1
        total = len(search_vars['matches'])
        next_button.config(text=f"{current}/{total}")

    # Find Section Layout
    find_frame = tk.LabelFrame(right_frame, text="Find")
    find_frame.pack(pady=5)

    find_entry = tk.Entry(find_frame, width=25)
    find_entry.pack(pady=5)

    buttons_frame = tk.Frame(find_frame)
    buttons_frame.pack()

    tk.Button(buttons_frame, text="Find", width=10, command=find_text).pack(side=tk.LEFT, padx=5)
    next_button = tk.Button(buttons_frame, text="Next", width=10, command=find_next)
    next_button.pack(side=tk.LEFT, padx=5)
    next_button.config(state=tk.DISABLED)

    # Tags Dictionary
    tags_info = {
        "rcv": {"name": "Roll Call Vote", "color": "#ADD8E6"},  # Light Blue
        "requester": {"name": "Requester", "color": "#90EE90"},  # Light Green
        "request type=regular": {"name": "Request (Regular)", "color": "#FFFFE0"},  # Light Yellow
        "request type=journal": {"name": "Request (Journal)", "color": "#E6E6FA"},  # Lavender
        "request type=postponed": {"name": "Request (Postponed)", "color": "#FFDAB9"},  # Peach Puff
        "request type=unpostponed": {"name": "Request (Un-Postponed)", "color": "#FFDAB9"},  # Peach Puff
        "request type=quorum_call": {"name": "Request (Quorum Call)", "color": "#FFA07A"},  # Light Salmon
        "request type=quorum_not_present": {"name": "Request (Quorum Not Present)", "color": "#FFA07A"},  # Light Salmon
        "request type=auto": {"name": "Request (Auto)", "color": "#FFE4E1"},  # Misty Rose
        "override": {"name": "Override", "color": "#FFC0CB"},  # Pink
    }

    # Tagging Section
    tagging_frame = tk.LabelFrame(right_frame, text="Tagging")
    tagging_frame.pack(pady=5)

    def add_tag(tag_code, selected_rcv=None):
        if not selected_rcv:
            if not last_selected_rcv[0]:
                messagebox.showwarning("No RCV Selected", "Please select an RCV first.")
                return
            selected_rcv = last_selected_rcv[0]

        if not validate_tag_add(selected_rcv, tag_code):
            return

        tag_info = tags_info.get(tag_code, {})
        tag_color = tag_info.get('color', 'gray')

        if tag_code == 'rcv':
            start_index, end_index = find_rcv(selected_rcv)

        else:
            try:
                start_index = text_widget.index(tk.SEL_FIRST)
                end_index = text_widget.index(tk.SEL_LAST)

            except tk.TclError:
                messagebox.showwarning("No Text Selected", f"Please select text to tag for '{tag_code}'.")
                return

        # Create unique mark names
        start_mark = f"start_{tag_code}_{selected_rcv}"
        end_mark = f"end_{tag_code}_{selected_rcv}"

        # Set marks at start and end indices with appropriate gravity
        text_widget.mark_set(start_mark, start_index)
        text_widget.mark_gravity(start_mark, tk.LEFT)  # Mark stays before inserted text
        text_widget.mark_set(end_mark, end_index)
        text_widget.mark_gravity(end_mark, tk.RIGHT)  # Mark stays after inserted text

        # Insert opening tag at start_mark
        opening_tag = f"<{tag_code} rcv={selected_rcv}>"
        text_widget.insert(start_mark, opening_tag)

        # Insert closing tag at end_mark
        closing_tag = f"<\\{tag_code} rcv={selected_rcv}>"
        text_widget.insert(end_mark, closing_tag)

        # Apply tag styling from start_mark to end_mark
        start_highlight_index = text_widget.index(start_mark)
        end_highlight_index = text_widget.index(end_mark)

        # Apply tag styling
        highlight_tag = f"{tag_code}_{selected_rcv}_{start_highlight_index}"
        text_widget.tag_add(highlight_tag, start_highlight_index, end_highlight_index)
        text_widget.tag_config(highlight_tag, background=tag_color)

        # Clean up marks (optional)
        text_widget.mark_unset(start_mark)
        text_widget.mark_unset(end_mark)

        # Update RCV tags
        rcv_tags[selected_rcv].add(tag_code)

    def find_rcv(rcv):
        pattern = rf'\[.*?(?:Roll\s*No\.?|Rollcall\s*Vote\s*No\.).*?{rcv}.*?\]'
        content = text_widget.get("1.0", tk.END)
        match = re.search(pattern, content, flags=re.IGNORECASE)
        if match:
            start_index = text_widget.search(match.group(), "1.0", tk.END)
            end_index = f"{start_index}+{len(match.group())}c"
            return start_index, end_index
        else:
            messagebox.showinfo("Not Found", f"RCV {rcv} not found in the text.")
            return None, None


    def validate_tag_add(rcv, tag_code):
        errors = []
        tags_applied = rcv_tags[rcv]

        if 'override' in tags_applied:
            return True

        if tag_code in tags_applied:
            errors.append(f"'{tag_code}' has already been added for RCV {rcv}.")

        if 'rcv' not in tags_applied and tag_code != 'rcv':
            errors.append(f"Please add 'rcv' for RCV {rcv} first.")

        if errors:
            messagebox.showwarning("Validation Failed", "\n".join(errors))
            return False

        return True

    def validate_tag_final():
        errors = []

        for rcv, tags_applied in rcv_tags.items():
            if 'override' in tags_applied:
                continue

            if 'rcv' not in tags_applied:
                errors.append(f"RCV {rcv}: Missing 'rcv'.")
                continue

            if 'requester type=regular' in tags_applied:
                if 'requester' not in tags_applied:
                    errors.append(f"RCV {rcv}: Missing 'requester'.")
                for tag in tags_applied:
                    if tag.startswith('request type=') and tag != 'request type=regular':
                        errors.append(f"RCV {rcv}: 'request type=regular' cannot be combined with '{tag}'.")

            if 'requester type=journal' in tags_applied:
                if 'requester' not in tags_applied:
                    errors.append(f"RCV {rcv}: Missing 'requester'.")
                for tag in tags_applied:
                    if tag.startswith('request type=') and tag != 'request type=journal':
                        errors.append(f"RCV {rcv}: 'request type=journal' cannot be combined with '{tag}'.")

            if 'requester type=postponed' or 'requester type=unpostponed' in tags_applied:
                if 'requester' not in tags_applied:
                    errors.append(f"RCV {rcv}: Missing 'requester'.")
                if ('requester type=postponed' not in tags_applied
                    or 'request type=unpostponed' not in tags_applied):
                    errors.append(f"RCV {rcv}: Missing 'request type=postponed' or 'request type=unpostponed'.")
                for tag in tags_applied:
                    if tag.startswith('request type=') and tag != 'request type=postponed' and tag != 'request type=unpostponed':
                        errors.append(f"RCV {rcv}: 'request type=postponed' and 'request type=unpostponed' cannot be combined with '{tag}'.")

            if 'requester type=quorum_call' in tags_applied:
                if 'requester' not in tags_applied:
                    errors.append(f"RCV {rcv}: Missing 'requester'.")
                for tag in tags_applied:
                    if tag.startswith('request type=') and tag != 'request type=quorum_call':
                        errors.append(f"RCV {rcv}: 'request type=quorum_call' cannot be combined with '{tag}'.")

            if 'requester type=quorum_not_present' in tags_applied:
                if 'requester' not in tags_applied:
                    errors.append(f"RCV {rcv}: Missing 'requester'.")
                for tag in tags_applied:
                    if tag.startswith('request type=') and tag != 'request type=quorum_not_present':
                        errors.append(f"RCV {rcv}: 'request type=quorum_not_present' cannot be combined with '{tag}'.")

            if 'requester type=auto' in tags_applied:
                for tag in tags_applied:
                    if tag.startswith('request type=') and tag != 'request type=auto':
                        errors.append(f"RCV {rcv}: 'request type=auto' cannot be combined with '{tag}'.")

        if errors:
            messagebox.showwarning("Validation Failed", "\n".join(errors))
            return False

        messagebox.showinfo("Validation Passed", "All tags have been validated successfully.")
        return True

    # Create tagging buttons
    for code, info in tags_info.items():
        tk.Button(tagging_frame, text=info['name'], width=25,
                  command=lambda c=code: add_tag(c)).pack(padx=5, pady=2)

    # Export Frame
    export_frame = tk.LabelFrame(right_frame, text="Export")
    export_frame.pack(pady=5)

    tk.Button(export_frame, text="Validate", width=25, command=validate_tag_final).pack(padx=5, pady=5)

    def save_file():
        if not validate_tag_final():
            return
        current_content = text_widget.get("1.0", tk.END)
        base_name = os.path.splitext(os.path.basename(filepath))[0]
        new_filename = f"{base_name}_annotated.txt"
        save_path = filedialog.asksaveasfilename(
            initialdir=os.path.dirname(filepath),
            initialfile=new_filename,
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt")]
        )
        if save_path:
            with open(save_path, 'w', encoding='utf-8') as file:
                file.write(current_content)
            messagebox.showinfo("Saved", f"File saved successfully as {os.path.basename(save_path)}.")

    tk.Button(export_frame, text="Save", width=25, command=save_file).pack(padx=5, pady=5)

    main_win.mainloop()

def view_file():
    filepath = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if not filepath:
        return

    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()
    except Exception as e:
        messagebox.showerror("Error", f"Failed to open the file.\nError: {e}")
        return

    tag_pattern = re.compile(r'<\\?(\w+)\s+(\d+)>')
    tags = list(tag_pattern.finditer(content))

    if not tags:
        messagebox.showinfo("No Tags Found", "No tags were found in the selected file.")
        return

    rcv_tags = {}
    for i, tag_match in enumerate(tags):
        tag, rcv = tag_match.group(1), tag_match.group(2)
        if rcv not in rcv_tags:
            rcv_tags[rcv] = []

        start_pos = tag_match.end()
        if i + 1 < len(tags):
            end_pos = tags[i + 1].start()
        else:
            end_pos = len(content)

        text_between = content[start_pos:end_pos].strip()
        rcv_tags[rcv].append((f"<{tag} {rcv}>", text_between))

    sorted_rcvs = sorted(rcv_tags.items(), key=lambda item: int(item[0]))

    view_win = tk.Toplevel()
    view_win.title(f"View File - {os.path.basename(filepath)}")

    text_area = tk.Text(view_win, wrap=tk.WORD, state=tk.NORMAL)
    text_area.pack(fill=tk.BOTH, expand=True)

    for rcv, tags_with_text in sorted_rcvs:
        text_area.insert(tk.END, f"RCV {rcv}:\n")
        for tag, text in tags_with_text:
            text_area.insert(tk.END, f"{tag}\n{text}\n")
        text_area.insert(tk.END, "\n")

def main():
    global root
    root = tk.Tk()
    root.title(f"CREC Annotator {version}")
    tk.Button(root, text="Annotate File", command=annotate_file).pack(padx=100, pady=20)
    tk.Button(root, text="View File", command=view_file).pack(padx=100, pady=20)
    root.mainloop()

if __name__ == "__main__":
    main()