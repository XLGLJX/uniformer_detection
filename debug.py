# # import cv2
# # from tqdm import tqdm
# # from PIL import Image as pImage
# # video_path = r'F:\web_app\FaceForensics-Detection_Website\media\in_out_videos\manipulate\Deepfakes\c40\videos\183_253.mp4'
# # reader = cv2.VideoCapture(video_path)
# # # fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
# # fourcc = int(cv2.VideoWriter_fourcc(*'H264'))  # VideoWriter_fourcc为视频编解码器
# # # fourcc = cv2.VideoWriter_fourcc(*'MJPG')
# # fps = reader.get(cv2.CAP_PROP_FPS)
# # num_frames = int(reader.get(cv2.CAP_PROP_FRAME_COUNT))
# # writer = None
# # end_frame = None
# # end_frame = end_frame if end_frame else num_frames
# # frame_num = 0
# # start_frame = 0
# # sequence_length = 30
# # # assert宏的原型定义在assert.h中，其作用是如果它的条件返回错误，则终止程序执行.
# # assert start_frame < num_frames - 1
# # pbar = tqdm(total=end_frame - start_frame)
# # frames = []
# # while reader.isOpened():
# #     _, image = reader.read()
# #     if image is None:
# #         break
# #     frame_num += 1
# #     frames.append(image)
# #     if frame_num < start_frame:
# #         continue
# #     pbar.update(1)
# # pbar.close()

# # frame_extract = []
# # video_file_name_only = video_path.split('\\')[-1].split('.')[0]

# # for i in range(1, sequence_length + 1):
# #     frame = frames[i]
# #     image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
# #     img = pImage.fromarray(image, 'RGB')
# #     image_name = video_file_name_only + "_preprocessed_" + str(i) + '.png'
# #     image_path = 'F:/web_app/FaceForensics-Detection_Website/preprocess_images/'  + image_name
# #     print(image_path)
# #     img.save(image_path)
# #     frame_extract.append(image_name)
# # print("<=== | Videos Splitting Done | ===>")

# #mb-3 mb-lg-0
# <div class="row justify-content-center no-gutters">
# 				<div class="col-lg-6">
# 					<img class="img-fluid mb-3 mb-lg-0" src="{% static '../media/images/deepfake.png' %}" alt="" />
# 				</div>
# 				<div class="col-lg-6 order-lg-first">
# 					<div class="bg-black text-center h-100 project">
# 						<div class="d-flex h-100">
# 							<div class="project-text w-100 my-auto text-center text-lg-right">
# 								<h4 class="text-white"><a href="https://en.wikipedia.org/wiki/Deepfake">Deepfake</a></h4>
# 								<p class="mb-0 text-white-50">
# 							        Deepfakes(“深度学习”和“假货”的合成词)是合成媒体,其中现有图像或视频中的人物被替换为其他人的肖像。虽然伪造内容的行为并不新鲜,但deepfakes利用机器学习和人工智能的强大技术来操纵或生成具有很高欺骗潜力的视觉和音频内容。
# 								</p>
# 								<hr class="d-none d-lg-block mb-0 mr-0" />
# 							</div>
# 						</div>
# 					</div>
# 				</div>
# 			</div>