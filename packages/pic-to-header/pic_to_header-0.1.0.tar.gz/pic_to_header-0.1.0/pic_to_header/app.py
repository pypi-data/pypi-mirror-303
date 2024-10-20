import streamlit as st
import os
from core import process_header_image

def main():
    st.markdown("""

<div align="center">

# Pic-to-Header

![Pic-to-Header Result](https://raw.githubusercontent.com/Sunwood-ai-labs/pic-to-header/refs/heads/main/assets/result.png)

[![GitHub license](https://img.shields.io/github/license/Sunwood-ai-labs/pic-to-header)](https://github.com/Sunwood-ai-labs/pic-to-header/blob/main/LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/Sunwood-ai-labs/pic-to-header)](https://github.com/Sunwood-ai-labs/pic-to-header/stargazers)
[![GitHub issues](https://img.shields.io/github/issues/Sunwood-ai-labs/pic-to-header)](https://github.com/Sunwood-ai-labs/pic-to-header/issues)

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![OpenCV](https://img.shields.io/badge/opencv-%23white.svg?style=for-the-badge&logo=opencv&logoColor=white)

</div>

Pic-to-Headerは、マスク画像と入力画像を使用してヘッダー画像を生成するPythonアプリケーションです。

                """, unsafe_allow_html=True)
    st.write("マスク画像と入力画像をアップロードして、ヘッダー画像を生成します。")

    input_image = st.file_uploader("入力画像をアップロード", type=["png", "jpg", "jpeg"])
    mask_image = st.file_uploader("マスク画像をアップロード", type=["png", "jpg", "jpeg"])

    if input_image is not None and mask_image is not None:
        if st.button("ヘッダー画像を生成"):
            # 一時ファイルとして保存
            input_path = f"temp_input.{input_image.name.split('.')[-1]}"
            mask_path = f"temp_mask.{mask_image.name.split('.')[-1]}"
            output_path = "output_header.png"

            with open(input_path, "wb") as f:
                f.write(input_image.getbuffer())
            with open(mask_path, "wb") as f:
                f.write(mask_image.getbuffer())

            # 画像処理
            process_header_image(input_path, mask_path, output_path)

            # 結果を表示
            st.image(output_path, caption="生成されたヘッダー画像")
            
            # ダウンロードボタンを追加
            with open(output_path, "rb") as file:
                btn = st.download_button(
                    label="ヘッダー画像をダウンロード",
                    data=file,
                    file_name="header_image.png",
                    mime="image/png"
                )

            # 一時ファイルを削除
            os.remove(input_path)
            os.remove(mask_path)
            os.remove(output_path)

if __name__ == "__main__":
    main()
