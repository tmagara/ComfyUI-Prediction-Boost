# ComfyUI-Prediction-Boost
Modify noise prediction to make image brighter on Stable Diffusion.
This is a custom node for ComfyUI.

# Method
We use xₜ⊥Ɛ̃(the vector component of xₜ perpendicular to Ɛ̃) to boost up the image part of xₜ by this:

Ɛ̃ ← Ɛ̃ - boost_scale * (xₜ⊥Ɛ̃)


# Result
- model: Animagine XL V3.1<https://civitai.com/models/260267/animagine-xl-v31>
- seed: 42
- steps: 25
- cfg: 3.0
- sampler: dpmpp_2m
- scheduler: karras
- negative prompt: flat design, early sketch, PTSD, stain, signature

- prompt: original, "the aquarium girl"

||||||
| --- | --- | --- | --- | --- |
| boost=0.0 | [![original, "the aquarium girl" (0)](samples/thumbnails/ComfyUI_00817_.png)](samples/ComfyUI_00817_.png) | [![original, "the aquarium girl" (1)](samples/thumbnails/ComfyUI_00818_.png)](samples/ComfyUI_00818_.png) | [![original, "the aquarium girl" (2)](samples/thumbnails/ComfyUI_00819_.png)](samples/ComfyUI_00819_.png) | [![original, "the aquarium girl" (3)](samples/thumbnails/ComfyUI_00820_.png)](samples/ComfyUI_00820_.png) |
| boost=0.1 | [![original, "the aquarium girl" (0)](samples/thumbnails/ComfyUI_00837_.png)](samples/ComfyUI_00837_.png) | [![original, "the aquarium girl" (1)](samples/thumbnails/ComfyUI_00838_.png)](samples/ComfyUI_00838_.png) | [![original, "the aquarium girl" (2)](samples/thumbnails/ComfyUI_00839_.png)](samples/ComfyUI_00839_.png) | [![original, "the aquarium girl" (3)](samples/thumbnails/ComfyUI_00840_.png)](samples/ComfyUI_00840_.png) |

- prompt: original, "the rainy days"

||||||
| --- | --- | --- | --- | --- |
| boost=0.0 | [![original, "the rainy days" (0)](samples/thumbnails/ComfyUI_00821_.png)](samples/ComfyUI_00821_.png) | [![original, "the rainy days" (1)](samples/thumbnails/ComfyUI_00822_.png)](samples/ComfyUI_00822_.png) | [![original, "the rainy days" (2)](samples/thumbnails/ComfyUI_00823_.png)](samples/ComfyUI_00823_.png) | [![original, "the rainy days" (3)](samples/thumbnails/ComfyUI_00824_.png)](samples/ComfyUI_00824_.png) |
| boost=0.1 | [![original, "the rainy days" (0)](samples/thumbnails/ComfyUI_00841_.png)](samples/ComfyUI_00841_.png) | [![original, "the rainy days" (1)](samples/thumbnails/ComfyUI_00842_.png)](samples/ComfyUI_00842_.png) | [![original, "the rainy days" (2)](samples/thumbnails/ComfyUI_00843_.png)](samples/ComfyUI_00843_.png) | [![original, "the rainy days" (3)](samples/thumbnails/ComfyUI_00844_.png)](samples/ComfyUI_00844_.png) |

- prompt: original, "botanical cafe"

||||||
| --- | --- | --- | --- | --- |
| boost=0.0 | [![original, "botanical cafe" (0)](samples/thumbnails/ComfyUI_00825_.png)](samples/ComfyUI_00825_.png) | [![original, "botanical cafe" (1)](samples/thumbnails/ComfyUI_00826_.png)](samples/ComfyUI_00826_.png) | [![original, "botanical cafe" (2)](samples/thumbnails/ComfyUI_00827_.png)](samples/ComfyUI_00827_.png) | [![original, "botanical cafe" (3)](samples/thumbnails/ComfyUI_00828_.png)](samples/ComfyUI_00828_.png) |
| boost=0.1 | [![original, "botanical cafe" (0)](samples/thumbnails/ComfyUI_00845_.png)](samples/ComfyUI_00845_.png) | [![original, "botanical cafe" (1)](samples/thumbnails/ComfyUI_00846_.png)](samples/ComfyUI_00846_.png) | [![original, "botanical cafe" (2)](samples/thumbnails/ComfyUI_00847_.png)](samples/ComfyUI_00847_.png) | [![original, "botanical cafe" (3)](samples/thumbnails/ComfyUI_00848_.png)](samples/ComfyUI_00848_.png) |

- prompt: original, "across the shore"

||||||
| --- | --- | --- | --- | --- |
| boost=0.0 | [![original, "across the shore" (0)](samples/thumbnails/ComfyUI_00829_.png)](samples/ComfyUI_00829_.png) | [![original, "across the shore" (1)](samples/thumbnails/ComfyUI_00830_.png)](samples/ComfyUI_00830_.png) | [![original, "across the shore" (2)](samples/thumbnails/ComfyUI_00831_.png)](samples/ComfyUI_00831_.png) | [![original, "across the shore" (3)](samples/thumbnails/ComfyUI_00832_.png)](samples/ComfyUI_00832_.png) |
| boost=0.1 | [![original, "across the shore" (0)](samples/thumbnails/ComfyUI_00849_.png)](samples/ComfyUI_00849_.png) | [![original, "across the shore" (1)](samples/thumbnails/ComfyUI_00850_.png)](samples/ComfyUI_00850_.png) | [![original, "across the shore" (2)](samples/thumbnails/ComfyUI_00851_.png)](samples/ComfyUI_00851_.png) | [![original, "across the shore" (3)](samples/thumbnails/ComfyUI_00852_.png)](samples/ComfyUI_00852_.png) |

