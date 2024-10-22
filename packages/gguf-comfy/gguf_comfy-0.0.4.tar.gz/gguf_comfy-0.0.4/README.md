### ComfyUI GGUF

custom node diagram generator (image/audio/video)

#### download the portal via
```
py -m gguf_comfy
```

![screenshot](https://raw.githubusercontent.com/calcuis/gguf-comfy/master/gguf.png)

- decompress the 7z bundle file: Extract All... (it includes everything you need to run a model)
- you could either get the dry run pack [here](https://huggingface.co/calcuis/flux1-gguf/tree/main) or pick them one-by-one from the original source below
- download [flux1-dev-Q4_0.gguf](https://huggingface.co/city96/FLUX.1-dev-gguf/blob/main/flux1-dev-Q4_0.gguf) (6.32GB); pull it to ./ComfyUI/models/unet
- download [clip_l.safetensors](https://huggingface.co/comfyanonymous/flux_text_encoders/blob/main/clip_l.safetensors) (234MB) and [t5xxl_fp8_e4m3fn.safetensors](https://huggingface.co/comfyanonymous/flux_text_encoders/blob/main/t5xxl_fp8_e4m3fn.safetensors) (4.55GB); pull them to ./ComfyUI/models/clip
- download [ae.safetensors](https://huggingface.co/black-forest-labs/FLUX.1-schnell/blob/main/ae.safetensors) (319MB); pull it to ./ComfyUI/models/vae
- run the .bat file under the main directory (it will activate the py backend as well as the js frontend)
- drag [gguf-workflow.json](https://github.com/calcuis/gguf-comfy/blob/main/gguf-workflow.json) to the activated browser

You are good to GO! (now you can run flux1 with the cheapest Nvidia GPU or merely CPU) ENJOY!
##### Reference: [comfyanonymous](https://github.com/comfyanonymous/ComfyUI) [city96](https://github.com/city96/ComfyUI-GGUF)