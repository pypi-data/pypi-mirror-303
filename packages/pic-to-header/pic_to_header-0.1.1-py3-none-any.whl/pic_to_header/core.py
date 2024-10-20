import cv2
import numpy as np
import argparse
import os
from loguru import logger

def process_header_image(input_image_path, mask_image_path, output_image_path):
    logger.info(f"処理を開始します: 入力画像={input_image_path}, マスク画像={mask_image_path}")
    
    # 入力画像を読み込む
    input_image = cv2.imread(input_image_path, cv2.IMREAD_UNCHANGED)
    logger.info(f"入力画像のサイズ: {input_image.shape}")
    
    # マスク画像を読み込む（グレースケールではなく、アルファチャンネル付きで）
    mask_image = cv2.imread(mask_image_path, cv2.IMREAD_UNCHANGED)
    logger.info(f"マスク画像のサイズ: {mask_image.shape}")
    
    # マスク画像を入力画像と同じサイズにリサイズ
    mask_image = cv2.resize(mask_image, (input_image.shape[1], input_image.shape[0]))
    logger.info(f"リサイズ後のマスク画像のサイズ: {mask_image.shape}")
    
    # 入力画像にアルファチャンネルがない場合は追加
    if input_image.shape[2] == 3:
        logger.info("入力画像にアルファチャンネルを追加します")
        input_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2BGRA)
    
    # マスク画像にアルファチャンネルがない場合は追加
    if mask_image.shape[2] == 3:
        logger.info("マスク画像にアルファチャンネルを追加します")
        mask_image = cv2.cvtColor(mask_image, cv2.COLOR_BGR2BGRA)
    
    # マスク画像のアルファチャンネルを取得
    mask_alpha = mask_image[:, :, 3]
    
    # 入力画像のアルファチャンネルを更新
    # マスクのアルファ値を使って元の画像のアルファ値を減算
    input_image[:, :, 3] = np.maximum(input_image[:, :, 3] - mask_alpha, 0)
    
    # 結果を保存
    cv2.imwrite(output_image_path, input_image)
    logger.info(f"処理が完了しました。出力画像: {output_image_path}")

    return output_image_path

if __name__ == "__main__":
    logger.add("process.log", rotation="1 MB")  # ログファイルの設定

    parser = argparse.ArgumentParser(description='画像にマスクを適用してヘッダー画像を生成します。')
    parser.add_argument('input_image', help='入力画像のパス')
    parser.add_argument('mask_image', help='マスク画像のパス')
    parser.add_argument('output_image', help='出力画像のパス')
    args = parser.parse_args()

    if not os.path.exists(args.input_image):
        logger.error(f"エラー: 入力画像が見つかりません: {args.input_image}")
    elif not os.path.exists(args.mask_image):
        logger.error(f"エラー: マスク画像が見つかりません: {args.mask_image}")
    else:
        try:
            result = process_header_image(args.input_image, args.mask_image, args.output_image)
            logger.success(f"処理が成功しました。結果: {result}")
        except Exception as e:
            logger.exception(f"エラーが発生しました: {str(e)}")
