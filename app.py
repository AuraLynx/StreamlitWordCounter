import streamlit as st
import re

def remove_spaces(input_string: str):
    pattern = r"[\s\u3000]+"
    return re.sub(pattern, '', input_string)

def count_manuscript_pages(text: str) -> int:
    char_per_page = 400

    char_count = len(text)

    pages = char_count // char_per_page
    if char_count % char_per_page != 0:
        pages += 1
    return pages

def count_paragraphs(text: str):
    lines = text.split('\n')
    
    paragraphs = []
    paragraph = []

    for line in lines:
        if line.strip():
            paragraph.append(line)
        else:
            if paragraph:
                paragraphs.append(paragraph)
                paragraph = []
    
    if paragraph:
        paragraphs.append(paragraph)

    return len(paragraphs)

def line_counter(text: str) -> int:
    _lines = len(text) // 40
    if len(text) % 40 != 0:
        _lines += 1
    return _lines

def word_counter() -> dict:
    text = st.session_state['text']
    st.session_state['length_with_space'] = len(text)
    st.session_state['length_wo_space'] = len(remove_spaces(text))
    st.session_state['lines'] = line_counter(text)
    st.session_state['paragraphs'] = count_paragraphs(text)
    st.session_state['manuscript'] = count_manuscript_pages(text)

def init_session_state():
    st.session_state['length_with_space'] = 0
    st.session_state['length_wo_space'] = 0
    st.session_state['lines'] = None
    st.session_state['paragraphs'] = None
    st.session_state['manuscript'] = None

def main():
    init_session_state()
    st.title('文字数カウンター')
    st.session_state['text'] = st.text_area(
        "ここに文字数をカウントしたい文章を貼り付けます",
        height=250,
        on_change=word_counter,
    )
    word_counter()
    with st.container(border=True):
        col1, col2, _ = st.columns(3)
        with col1:
            st.write("文字数（スペース込み）")
            st.write("文字数（スペース無視）")
            st.write("行数")
            st.write("段落数")
            st.write("原稿用紙換算(400字x?枚)")

        with col2:
            st.write(st.session_state['length_with_space'])
            st.write(st.session_state['length_wo_space'])
            st.write(st.session_state['lines'])
            st.write(st.session_state['paragraphs'])
            st.write(st.session_state['manuscript'])


if __name__ == '__main__':
    main()
