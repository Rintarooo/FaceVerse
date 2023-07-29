# Fix Bug and Error

```bash
root@###:/app# python tracking_offline.py --input example/videos/test.mp4 --res_folder example/video_results --version 2 --use_simplification
Traceback (most recent call last):
  File "/app/tracking_offline.py", line 199, in <module>
    tracking(args, device)
  File "/app/tracking_offline.py", line 31, in tracking
    offreader = OfflineReader(args.input)
  File "/app/data_reader.py", line 67, in __init__
    self.tracker = Tracker(self.width, self.height, threshold=None, max_threads=1,
  File "/app/third_libs/OpenSeeFace/tracker.py", line 526, in __init__
    self.retinaface = RetinaFaceDetector(model_path=os.path.join(model_base_path, "retinaface_640x640_opt.onnx"), json_path=os.path.join(model_base_path, "priorbox_640x640.json"), threads=max(max_threads,4), top_k=max_faces, res=(640, 640))
  File "/app/third_libs/OpenSeeFace/retinaface.py", line 69, in __init__
    self.session = onnxruntime.InferenceSession(model_path, sess_options=options)
  File "/usr/local/lib/python3.9/site-packages/onnxruntime/capi/onnxruntime_inference_collection.py", line 396, in __init__
    raise e
  File "/usr/local/lib/python3.9/site-packages/onnxruntime/capi/onnxruntime_inference_collection.py", line 383, in __init__
    self._create_inference_session(providers, provider_options, disabled_optimizers)
  File "/usr/local/lib/python3.9/site-packages/onnxruntime/capi/onnxruntime_inference_collection.py", line 415, in _create_inference_session
    raise ValueError(
ValueError: This ORT build has ['TensorrtExecutionProvider', 'CUDAExecutionProvider', 'CPUExecutionProvider'] enabled. Since ORT 1.9, you are required to explicitly set the providers parameter when instantiating InferenceSession. For example, onnxruntime.InferenceSession(..., providers=['TensorrtExecutionProvider', 'CUDAExecutionProvider', 'CPUExecutionProvider'], ...)
```
- https://self-development.info/%E3%80%90python%E3%81%A7%E3%83%87%E3%82%A3%E3%83%BC%E3%83%97%E3%83%95%E3%82%A7%E3%82%A4%E3%82%AF%E5%8B%95%E7%94%BB%E4%BD%9C%E6%88%90%E3%80%91simswap%E3%81%AE%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88/


