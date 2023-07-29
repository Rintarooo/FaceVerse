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
<!-- - https://self-development.info/%E3%80%90python%E3%81%A7%E3%83%87%E3%82%A3%E3%83%BC%E3%83%97%E3%83%95%E3%82%A7%E3%82%A4%E3%82%AF%E5%8B%95%E7%94%BB%E4%BD%9C%E6%88%90%E3%80%91simswap%E3%81%AE%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88/ -->
- https://www.jianshu.com/p/f7f01904d96d



```bash
oot@be1d1b4e3c28:/app# python tracking_offline.py --input example/videos/test.mp4 --res_folder example/video_results --version 2 --use_simplification
2023-07-29 16:48:51.018219359 [E:onnxruntime:, inference_session.cc:1644 operator()] Exception during initialization: /onnxruntime_src/onnxruntime/contrib_ops/cuda/fused_conv.cc:19 onnxruntime::contrib::cuda::FusedConv<T>::FusedConv(const onnxruntime::OpKernelInfo&) [with T = float] [ONNXRuntimeError] : 2 : INVALID_ARGUMENT : unsupported conv activation mode "LeakyRelu"

Traceback (most recent call last):
  File "/app/tracking_offline.py", line 199, in <module>
    tracking(args, device)
  File "/app/tracking_offline.py", line 31, in tracking
    offreader = OfflineReader(args.input)
  File "/app/data_reader.py", line 67, in __init__
    self.tracker = Tracker(self.width, self.height, threshold=None, max_threads=1,
  File "/app/third_libs/OpenSeeFace/tracker.py", line 526, in __init__
    self.retinaface = RetinaFaceDetector(model_path=os.path.join(model_base_path, "retinaface_640x640_opt.onnx"), json_path=os.path.join(model_base_path, "priorbox_640x640.json"), threads=max(max_threads,4), top_k=max_faces, res=(640, 640))
  File "/app/third_libs/OpenSeeFace/retinaface.py", line 72, in __init__
    self.session = onnxruntime.InferenceSession(model_path, sess_options=options, providers=['CUDAExecutionProvider'])
  File "/usr/local/lib/python3.9/site-packages/onnxruntime/capi/onnxruntime_inference_collection.py", line 383, in __init__
    self._create_inference_session(providers, provider_options, disabled_optimizers)
  File "/usr/local/lib/python3.9/site-packages/onnxruntime/capi/onnxruntime_inference_collection.py", line 435, in _create_inference_session
    sess.initialize_session(providers, provider_options, disabled_optimizers)
onnxruntime.capi.onnxruntime_pybind11_state.RuntimeException: [ONNXRuntimeError] : 6 : RUNTIME_EXCEPTION : Exception during initialization: /onnxruntime_src/onnxruntime/contrib_ops/cuda/fused_conv.cc:19 onnxruntime::contrib::cuda::FusedConv<T>::FusedConv(const onnxruntime::OpKernelInfo&) [with T = float] [ONNXRuntimeError] : 2 : INVALID_ARGUMENT : unsupported conv activation mode "LeakyRelu"
```


# v3
```bash
root@be1d1b4e3c28:/app/faceversev3_jittor# python tracking_offline_cuda.py --input ../example/videos/test.mp4 --res_folder output/video --skip_frames 1
[i 0729 16:53:16.110665 04 lock.py:85] Create lock file:/root/.cache/jittor/jt1.3.8/g++9.4.0/py3.9.0/Linux-5.15.0-1xe2/IntelRXeonRCPUx1c/jittor.lock
[i 0729 16:53:16.133666 04 compiler.py:956] Jittor(1.3.8.5) src: /usr/local/lib/python3.9/site-packages/jittor
[i 0729 16:53:16.139089 04 compiler.py:957] g++ at /usr/bin/g++(9.4.0)
[i 0729 16:53:16.139404 04 compiler.py:958] cache_path: /root/.cache/jittor/jt1.3.8/g++9.4.0/py3.9.0/Linux-5.15.0-1xe2/IntelRXeonRCPUx1c/default
[i 0729 16:53:16.153283 04 __init__.py:411] Found nvcc(11.3.109) at /usr/local/cuda/bin/nvcc.
[i 0729 16:53:16.162461 04 __init__.py:411] Found addr2line(2.34) at /usr/bin/addr2line.
[i 0729 16:53:18.917334 04 compiler.py:1011] cuda key:cu11.3.109_sm_75
[i 0729 16:53:18.954972 04 compiler.py:34] Create cache dir: /root/.cache/jittor/jt1.3.8/g++9.4.0/py3.9.0/Linux-5.15.0-1xe2/IntelRXeonRCPUx1c/default/cu11.3.109_sm_75
[i 0729 16:53:18.955316 04 compiler.py:34] Create cache dir: /root/.cache/jittor/jt1.3.8/g++9.4.0/py3.9.0/Linux-5.15.0-1xe2/IntelRXeonRCPUx1c/default/cu11.3.109_sm_75/jit
[i 0729 16:53:18.955569 04 compiler.py:34] Create cache dir: /root/.cache/jittor/jt1.3.8/g++9.4.0/py3.9.0/Linux-5.15.0-1xe2/IntelRXeonRCPUx1c/default/cu11.3.109_sm_75/obj_files
[i 0729 16:53:18.955813 04 compiler.py:34] Create cache dir: /root/.cache/jittor/jt1.3.8/g++9.4.0/py3.9.0/Linux-5.15.0-1xe2/IntelRXeonRCPUx1c/default/cu11.3.109_sm_75/gen
[i 0729 16:53:18.956048 04 compiler.py:34] Create cache dir: /root/.cache/jittor/jt1.3.8/g++9.4.0/py3.9.0/Linux-5.15.0-1xe2/IntelRXeonRCPUx1c/default/cu11.3.109_sm_75/tmp
[i 0729 16:53:18.956281 04 compiler.py:34] Create cache dir: /root/.cache/jittor/jt1.3.8/g++9.4.0/py3.9.0/Linux-5.15.0-1xe2/IntelRXeonRCPUx1c/default/cu11.3.109_sm_75/checkpoints
[i 0729 16:53:50.785761 12 __init__.py:227] Total mem: 14.63GB, using 4 procs for compiling.
Compiling jittor_core(151/151) used: 124.017s eta: 0.000ss
[i 0729 16:55:55.345181 12 jit_compiler.cc:28] Load cc_path: /usr/bin/g++
[i 0729 16:55:57.818517 12 init.cc:62] Found cuda archs: [75,]
[i 0729 16:55:58.546869 12 compiler.py:34] Create cache dir: /root/.cache/jittor/cutt
[i 0729 16:55:58.593718 12 compile_extern.py:339] Downloading cutt...
Downloading https://codeload.github.com/Jittor/cutt/zip/v1.2 to /root/.cache/jittor/cutt/cutt-1.2.zip
296kB [00:00, 1.09MB/s]
[i 0729 16:55:58.884850 12 compile_extern.py:352] installing cutt...
Compiling libcutt(9/9) used: 17.650s eta: 0.000s
[i 0729 16:56:16.664216 12 compiler.py:34] Create cache dir: /root/.cache/jittor/jt1.3.8/g++9.4.0/py3.9.0/Linux-5.15.0-1xe2/IntelRXeonRCPUx1c/default/cu11.3.109_sm_75/custom_ops
Compiling gen_ops_cutt_transpose_cutt_test(4/4) used: 2.750s eta: 0.000s
[i 0729 16:56:19.520048 12 compiler.py:34] Create cache dir: /root/.cache/jittor/mkl
[i 0729 16:56:19.520389 12 compile_extern.py:73] Downloading mkl...
Downloading https://cg.cs.tsinghua.edu.cn/jittor/assets/dnnl_lnx_2.2.0_cpu_gomp.tgz to /root/.cache/jittor/mkl/dnnl_lnx_2.2.0_cpu_gomp.tgz
10.5MB [00:02, 4.41MB/s]                                                                                                  
Use time: 27.03 ms per iteration.
Example passed on CPU.
Compiling gen_ops_mkl_conv_mkl_test_mkl_conv_backward_w_mkl____hash3a7c79(7/7) used: 6.949s eta: 0.000ss
[i 0729 16:56:36.466392 12 compiler.py:34] Create cache dir: /root/.cache/jittor/jt1.3.8/g++9.4.0/py3.9.0/Linux-5.15.0-1xe2/IntelRXeonRCPUx1c/default/cu11.3.109_sm_75/cuda
Compiling libcuda_extern(3/3) used: 2.579s eta: 0.000s
Compiling gen_ops_cub_test_cub_argsort_cub_arg_reduce_cub_cu___hash770c74(6/6) used: 4.611s eta: 0.000s
Compiling gen_ops_cublas_acc_matmul_cublas_batched_matmul_cu___hashe0fa5d(8/8) used: 4.553s eta: 0.000s
Compiling gen_ops_cudnn_conv_cudnn_conv3d_backward_x_cudnn_c___hashd168ca(16/16) used: 11.132s eta: 0.000s
Compiling gen_ops_curand_random(4/4) used: 3.178s eta: 0.000s
Compiling gen_ops_cufft_fft(3/3) used: 2.275s eta: 0.000s
[i 0729 16:57:07.762003 12 cuda_flags.cc:49] CUDA enabled.

Compiling Operators(8/8) used: 16.3s eta:    0s 
INFO: Created TensorFlow Lite XNNPACK delegate for CPU.
OpenCV: FFMPEG: tag 0x5634504d/'MP4V' is not supported with codec id 12 and format 'mp4 / MP4 (MPEG-4 Part 14)'
OpenCV: FFMPEG: fallback to use tag 0x7634706d/'mp4v'
First frame: 1011 [2416 1506]

Compiling Operators(4/4) used: 8.32s eta:    0s 

Compiling Operators(85/85) used:  161s eta:    0s 

Compiling Operators(2/2) used: 5.31s eta:    0s 

Compiling Operators(1/1) used: 3.26s eta:    0s 

Compiling Operators(2/2) used: 5.31s eta:    0s 
Speed:136.2686,    1 /    2, 0.1216
qt.qpa.xcb: could not connect to display 
qt.qpa.plugin: Could not load the Qt platform plugin "xcb" in "/usr/local/lib/python3.9/site-packages/cv2/qt/plugins" even though it was found.
This application failed to start because no Qt platform plugin could be initialized. Reinstalling the application may fix this problem.

Available platform plugins are: xcb.

Aborted (core dumped)
```