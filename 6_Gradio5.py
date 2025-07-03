import gradio as gr

def add(num1, num2):
    return num1 + num2

interface = gr.Interface(
    fn=add,
    inputs = ['number', 'number'],   # 두 개의 값을 입력
    outputs = 'number',   # 한 개의 결과로 출력
    title='계산기',
    description='숫자 두 개를 입력하세요',
    flagging_mode="never"   # flag 를 하지 않음
)

interface.launch()