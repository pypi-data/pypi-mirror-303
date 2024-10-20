import argparse
import os
import sys
from loguru import logger
from .core import process_header_image

def main():
    # スクリプトのディレクトリをパスに追加
    script_dir = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(script_dir)
    
    parser = argparse.ArgumentParser(description='画像にマスクを適用してヘッダー画像を生成します。')
    parser.add_argument('input_image', help='入力画像のパス')
    parser.add_argument('mask_image', help='マスク画像のパス')
    parser.add_argument('output_image', help='出力画像のパス')
    args = parser.parse_args()

    # 入力ファイルパスを絶対パスに変換
    input_image = os.path.abspath(args.input_image)
    mask_image = os.path.abspath(args.mask_image)
    output_image = os.path.abspath(args.output_image)

    if not os.path.exists(input_image):
        logger.error(f"エラー: 入力画像が見つかりません: {input_image}")
    elif not os.path.exists(mask_image):
        logger.error(f"エラー: マスク画像が見つかりません: {mask_image}")
    else:
        try:
            result = process_header_image(input_image, mask_image, output_image)
            logger.success(f"処理が成功しました。結果: {result}")
        except Exception as e:
            logger.exception(f"エラーが発生しました: {str(e)}")

if __name__ == "__main__":
    main()
