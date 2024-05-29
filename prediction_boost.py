import torch


def _rejection(u, v):
    uv = torch.mean(u * v, dim=list(range(1, v.ndim)), keepdim=True)
    vv = torch.mean(v ** 2, dim=list(range(1, v.ndim)), keepdim=True) + 1.0e-05
    return u - (uv / vv) * v


def _normalize(u, v):
    uu = torch.mean(u ** 2, dim=list(range(1, u.ndim)), keepdim=True) + 1.0e-05
    vv = torch.mean(v ** 2, dim=list(range(1, v.ndim)), keepdim=True)
    return ((torch.relu(1 - vv) / uu) ** 0.5) * u


class PredictionBoost:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "model": ("MODEL",),
                "boost_scale": ("FLOAT", {"default": 0.0, "min": -1.0, "max": 1.0, "step": 0.01}),
            },
        }

    RETURN_TYPES = ("MODEL",)
    FUNCTION = "execute"
    CATEGORY = "advanced/model"

    def execute(self, model, boost_scale):
        do_normalize = "enable"
        def sampler_post_cfg_function(args):
            sigma = args["sigma"]
            input = args["input"]
            denoised = args["denoised"]
            cond_denoised = args["cond_denoised"]

            noise_pred = (input - denoised) / sigma
            noise_pred_cond = (input - cond_denoised) / sigma
            boost_denoised = _rejection(input, noise_pred_cond)
            if do_normalize == "enable":
                boost_denoised = _normalize(boost_denoised, noise_pred) * sigma
            return denoised + boost_scale * boost_denoised

        m = model.clone()
        m.set_model_sampler_post_cfg_function(sampler_post_cfg_function)
        return (m, )


