import gradio as gr


def bmi(name, height, weight, feeling):
    bmi_val = weight/((height/100)**2)
    result_emoticon = "😊" if bmi_val < 30 else "😢"
    output_str = "Hello 👋" + name + "...\n your BMI is.."+ str(bmi_val)
    txt = "Happy" if feeling else "Sad"
    return (output_str, result_emoticon, txt)

interface= gr.Interface(
    fn= bmi,
    inputs=["text", gr.inputs.Slider(1,200, label ="Weight in KGs") ,gr.inputs.Slider(1,200, label ="Height in CMs",),gr.inputs.Checkbox("Your Feeling Today")],
    outputs = ["text", "text", "text"],
    desciron =" Flag if you find any errors in output "
    )

interface.launch(debug = True)

