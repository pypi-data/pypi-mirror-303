import unittest
import os
import cv2
import numpy as np
from pic_to_header.core import process_header_image

class TestCore(unittest.TestCase):
    def setUp(self):
        self.input_image_path = 'test_input.png'
        self.mask_image_path = 'test_mask.png'
        self.output_image_path = 'test_output.png'

        # テスト用の入力画像を作成
        input_image = np.ones((100, 100, 3), dtype=np.uint8) * 255
        cv2.imwrite(self.input_image_path, input_image)

        # テスト用のマスク画像を作成
        mask_image = np.zeros((100, 100), dtype=np.uint8)
        mask_image[25:75, 25:75] = 255
        cv2.imwrite(self.mask_image_path, mask_image)

    def tearDown(self):
        # テスト用のファイルを削除
        for file in [self.input_image_path, self.mask_image_path, self.output_image_path]:
            if os.path.exists(file):
                os.remove(file)

    def test_process_header_image(self):
        # process_header_image 関数をテスト
        result = process_header_image(self.input_image_path, self.mask_image_path, self.output_image_path)

        # 出力ファイルが作成されたことを確認
        self.assertTrue(os.path.exists(self.output_image_path))

        # 出力画像を読み込み
        output_image = cv2.imread(self.output_image_path, cv2.IMREAD_UNCHANGED)

        # 出力画像が正しいサイズであることを確認
        self.assertEqual(output_image.shape[:2], (100, 100))

        # アルファチャンネルが正しく適用されていることを確認
        self.assertEqual(output_image.shape[2], 4)  # BGRAチャンネル
        
        # マスクが正しく適用されていることを確認
        np.testing.assert_array_equal(output_image[25:75, 25:75, 3], 255)
        np.testing.assert_array_equal(output_image[:25, :, 3], 0)
        np.testing.assert_array_equal(output_image[75:, :, 3], 0)
        np.testing.assert_array_equal(output_image[:, :25, 3], 0)
        np.testing.assert_array_equal(output_image[:, 75:, 3], 0)

if __name__ == '__main__':
    unittest.main()
