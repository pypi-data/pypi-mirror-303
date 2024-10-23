import torchvision.transforms
import torch
from PIL import Image
from typing import List
import torch.nn.functional as F
import cv2 as cv
import numpy as np

class MultiTransform():
    def __init__(self):
        pass

    def __call__(self, input):
        raise NotImplementedError()
    
    def __get_size__(self, imgs):
        if not hasattr(self, 'size'):
            if isinstance(imgs[0], torch.Tensor):
                self.size = (imgs[0].shape[1], imgs[0].shape[2])
            else:
                self.size = (imgs[0].size[1], imgs[0].size[0])
    
    def __reset__(self):
        raise NotImplementedError()

class Compose():
    def __init__(self, children:List[MultiTransform]):
        self.children = children
        pass

    def __call__(self, input):
        result = input
        for c in self.children:
            result = c(result)
        for c in self.children:
            c.__reset__()
        return result
    
    def __reset__(self):
        pass

class Normalize(MultiTransform):
    def __init__(self, mean, std, inplace = False):
        super().__init__()

        self.normalize = torchvision.transforms.Normalize(mean, std, inplace)
        self.__toTensor__ = ToTensor()
        self.__toPILImage__ = ToPILImage()

    def __call__(self, inputs):
        is_tensor = isinstance(inputs[0], torch.Tensor)
        if not is_tensor:
            inputs = self.__toTensor__(inputs)
        inputs = torch.stack(inputs)

        results = []
        for res in self.normalize(inputs):
            results.append(res)

        if not is_tensor:
            results = self.__toPILImage__(results)
        return results
    
    def __reset__(self):
        pass
    
class ToTensor(MultiTransform):
    def __init__(self):
        super().__init__()

        self.toTensor = torchvision.transforms.ToTensor()

    def __call__(self, images:Image):
        results = []
        for img in images:
            result = self.toTensor(img).float()
            results.append(result)
        return results
    
    def __reset__(self):
        pass
    
class CenterCrop(MultiTransform):
    def __init__(self, max_scale = 2):
        super().__init__()

        if max_scale < 1:
            raise Exception(f'max_scale expected to be greater than 1. Actual value is {max_scale})')
        self.max_scale = max_scale

        self.__toTensor__ = ToTensor()
        self.__toPILImage__ = ToPILImage()

        self.__reset__()

    def __call__(self, imgs):
        self.__get_size__(imgs)
    
        results = []

        is_tensor = isinstance(imgs[0], torch.Tensor)
        if not is_tensor:
            imgs = self.__toTensor__(imgs)
        
        for img in imgs:
            img_before = img.permute(1, 2, 0).numpy()

            w, h = self.size[1], self.size[0]
            new_w, new_h = int(np.round(w * self.__scale__)), int(np.round(h * self.__scale__))
            img_after = cv.resize(img_before, (new_w, new_h))

            cx, cy = new_w // 2, new_h // 2
            result = img_after[cy - h // 2: cy + h // 2, cx - w // 2: cx + w // 2]
            result = torch.tensor(result, dtype=img.dtype).permute(2, 0, 1)

            results.append(result)

        if not is_tensor:
            results = self.__toPILImage__(results)
            
        return results
    
    def __reset__(self):
        self.__scale__ = 1. + np.random.random() * (self.max_scale - 1.)

class RandomCrop(MultiTransform):
    def __init__(self, max_scale = 2):
        super().__init__()

        if max_scale < 1:
            raise Exception(f'max_scale expected to be greater than 1. Actual value is {max_scale})')
        self.max_scale = max_scale

        self.__toCVImage__ = ToCVImage()
        self.__toTensor__ = ToTensor()
        self.__toPILImage__ = ToPILImage()

        self.__reset__()

    def __call__(self, imgs):
        self.__get_size__(imgs)
    
        results = []

        is_tensor = isinstance(imgs[0], torch.Tensor)
        if not is_tensor:
            imgs = self.__toTensor__(imgs)
        
        #imgs = self.__toCVImage__(imgs)

        for img in imgs:
            img_before = img.permute(1, 2, 0).numpy()

            w, h = self.size[1], self.size[0]
            new_w, new_h = int(np.round(w * self.__scale__)), int(np.round(h * self.__scale__))
            img_after = cv.resize(img_before, (new_w, new_h))

            img_after = torch.tensor(img_after, dtype=img.dtype).permute(2, 0, 1)
            result = img_after[:, self.__sy__:self.__sy__ + h, self.__sx__:self.__sx__ + w]

            results.append(result)

        if not is_tensor:
            results = self.__toPILImage__(results)
            
        return results
    
    def __reset__(self):
        self.__scale__ = 1. + np.random.random() * (self.max_scale - 1.)
        if not hasattr(self, 'size'):
            self.__sx__ = 0
            self.__sy__ = 0
        else:
            w, h = self.size[1], self.size[0]
            new_w, new_h = self.__scale__ * self.size[1], self.__scale__ * self.size[0]
            self.__sx__ = int(np.round(np.random.random() * (new_w - w)))
            self.__sy__ = int(np.round(np.random.random () * (new_h - h)))

class Rotate(MultiTransform):
    def __init__(self, max_angle = 180, auto_scale:bool = True):
        super().__init__()

        self.max_angle = max_angle
        self.auto_scale = auto_scale

        self.__toTensor__ = ToTensor()
        self.__toPILImage__ = ToPILImage()

    def __call__(self, imgs):
        self.__get_size__(imgs)
        self.__reset__()
    
        results = []

        is_tensor = isinstance(imgs[0], torch.Tensor)
        if not is_tensor:
            imgs = self.__toTensor__(imgs)

        for img in imgs:
            img_before = img.permute(1, 2, 0).numpy()

            w, h = self.size[1], self.size[0]
            mat = cv.getRotationMatrix2D((w // 2, h // 2), self.__angle__, self.__scale__)
            img_after = cv.warpAffine(img_before, mat, (w, h))

            result = torch.tensor(img_after, dtype=img.dtype).permute(2, 0, 1)

            results.append(result)

        if not is_tensor:
            results = self.__toPILImage__(results)
            
        return results
    
    def __reset__(self):
        self.__angle__ = -self.max_angle + 2 * np.random.random() * self.max_angle

        w, h = self.size[1], self.size[0]
        t1 = np.sin(self.__angle__)
        new_w = w + np.abs(np.sin(self.__angle__ / 180 * np.pi) * w)
        new_h = h + np.abs(np.sin(self.__angle__ / 180 * np.pi) * h)

        self.__scale__ = 1.03 * np.max([new_w / w, new_h / h]) if self.auto_scale else 1.

class ToNumpy(MultiTransform):
    def __init__(self):
        super().__init__()

    def __call__(self, tensor:torch.Tensor):
        result = tensor.numpy()
        return result
    
    def __reset__(self):
        pass

class ToCVImage(MultiTransform):
    def __init__(self):
        super().__init__()

        self.__toTensor__ = ToTensor()

    def __call__(self, inputs) -> List[np.array]:
        is_tensor = isinstance(inputs[0], torch.Tensor)
        if not is_tensor:
            inputs = self.__toTensor__(inputs)
        results = []
        for img in inputs:
            result = np.asarray(img.permute(1, 2, 0), dtype = np.float32)
            results.append(result)
        return results
    
    def __reset__(self):
        pass

class ToPILImage(MultiTransform):
    def __init__(self):
        super().__init__()

        self.__toPILImage__ = torchvision.transforms.ToPILImage()

    def __call__(self, tensor:torch.Tensor):
        results = []
        for img in tensor:
            result = self.__toPILImage__(img)
            results.append(result)
        return results
    
    def __reset__(self):
        pass

class BGR2RGB(MultiTransform):
    def __init__(self):
        super().__init__()

        self.__toTensor__ = ToTensor()
        self.__toPILImage__ = ToPILImage()

    def __call__(self, inputs):
        is_tensor = isinstance(inputs[0], torch.Tensor)
        if not is_tensor:
            inputs = self.__toTensor__(inputs)

        results = []
        for input in inputs:
            result = torch.flip(input, (0,))
            results.append(result)

        if not is_tensor:
            results = self.__toPILImage__(results)
        return results
    
    def __reset__(self):
        pass

class RGB2BGR(BGR2RGB):
    pass

class Scale(MultiTransform):
    def __init__(self, scale):
        super().__init__()

        self.__toTensor__ = ToTensor()
        self.__toPILImage__ = ToPILImage()

        self.scale = scale

        self.__toCVImage__ = ToCVImage()

    def __call__(self, inputs):
        self.__get_size__(inputs)
        self.__reset__()
        is_tensor = isinstance(inputs[0], torch.Tensor)
        if not is_tensor:
            inputs = self.__toTensor__(inputs)

        results = []
        for input in self.__toCVImage__(inputs):
            w, h = self.size[1], self.size[0]
            new_w, new_h = int(np.round(self.scale * w)), int(np.round(self.scale * h))
            result = cv.resize(input, (new_w, new_h))
            results.append(result)

        results = self.__toTensor__(results)

        if not is_tensor:
            results = self.__toPILImage__(results)
        return results
    
    def __reset__(self):
        pass

class Resize(MultiTransform):
    def __init__(self, target_size:tuple[int, int], auto_crop:bool = True):
        super().__init__()

        self.__toTensor__ = ToTensor()
        self.__toPILImage__ = ToPILImage()
        self.__toCVImage__ = ToCVImage()

        self.target_size = target_size
        self.auto_crop = auto_crop

    def __call__(self, inputs):
        self.__get_size__(inputs)
        self.__reset__()
        is_tensor = isinstance(inputs[0], torch.Tensor)
        if not is_tensor:
            inputs = self.__toTensor__(inputs)

        results = []
        for input in self.__toCVImage__(inputs):
            w, h = self.size[1], self.size[0]
            if self.auto_crop:
                scale = np.max([self.target_size[0] / self.size[0], self.target_size[1] / self.size[1]])
                new_w, new_h = int(np.round(scale * w)), int(np.round(scale * h))
                result = cv.resize(input, (new_w, new_h))

                cx, cy = result.shape[1] // 2, result.shape[0] // 2
                result = result[cy-self.target_size[0]//2:cy+self.target_size[0]//2, cx-self.target_size[1]//2:cx+self.target_size[1]//2]
            else:
                new_w, new_h = self.target_size[1], self.target_size[0]
                result = cv.resize(input, (new_w, new_h))
            results.append(result)

        results = self.__toTensor__(results)

        if not is_tensor:
            results = self.__toPILImage__(results)
        return results
    
    def __reset__(self):
        pass

class Brightness(MultiTransform):
    def __init__(self, min_rel:float, max_rel:float):
        super().__init__()

        if min_rel < 0 or max_rel < 0 or min_rel > max_rel:
            raise Exception(f'min_rel and max_rel expected to be greater or equal 0. min_rel expected to be less or equal max_rel')

        self.__toTensor__ = ToTensor()
        self.__toPILImage__ = ToPILImage()

        self.min_rel = min_rel
        self.max_rel = max_rel

        self.__toCVImage__ = ToCVImage()

    def __call__(self, inputs):
        self.__get_size__(inputs)
        self.__reset__()
        is_tensor = isinstance(inputs[0], torch.Tensor)
        if not is_tensor:
            inputs = self.__toTensor__(inputs)

        is_color_image = inputs[0].shape[0] == 3

        results = []
        for input in self.__toCVImage__(inputs):
            if not is_color_image:
                input = cv.cvtColor(input, cv.COLOR_GRAY2BGR)
            hsv = cv.cvtColor(input, cv.COLOR_BGR2HSV)
            h, s, v = cv.split(hsv)

            v *= self.rel
            v[v > 1] = 1
            v[v < 0] = 0
            hsv = cv.merge((h, s, v))
            result = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)

            if not is_color_image:
                result = cv.cvtColor(result, cv.COLOR_BGR2GRAY)

            results.append(result)
        
        results = self.__toTensor__(results)
        
        if not is_tensor:
            results = self.__toPILImage__(results)
        return results
    
    def __reset__(self):
        self.rel = self.min_rel + np.random.random() * (self.max_rel - self.min_rel)

class Satturation(MultiTransform):
    def __init__(self, min_rel:float, max_rel:float):
        super().__init__()

        if min_rel < 0 or max_rel < 0 or min_rel > max_rel:
            raise Exception(f'min_rel and max_rel expected to be greater or equal 0. min_rel expected to be less or equal max_rel')

        self.__toTensor__ = ToTensor()
        self.__toPILImage__ = ToPILImage()

        self.min_rel = min_rel
        self.max_rel = max_rel

        self.__toCVImage__ = ToCVImage()

    def __call__(self, inputs):
        self.__get_size__(inputs)
        self.__reset__()
        is_tensor = isinstance(inputs[0], torch.Tensor)
        if not is_tensor:
            inputs = self.__toTensor__(inputs)

        is_color_image = inputs[0].shape[0] == 3

        results = []
        for input in self.__toCVImage__(inputs):
            if not is_color_image:
                input = cv.cvtColor(input, cv.COLOR_GRAY2BGR)
            hsv = cv.cvtColor(input, cv.COLOR_BGR2HSV)
            h, s, v = cv.split(hsv)

            s *= self.rel
            s[s > 1] = 1
            s[s < 0] = 0
            hsv = cv.merge((h, s, v))
            result = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)

            if not is_color_image:
                result = cv.cvtColor(result, cv.COLOR_BGR2GRAY)

            results.append(result)

        results = self.__toTensor__(results)

        if not is_tensor:
            results = self.__toPILImage__(results)
        return results
    
    def __reset__(self):
        self.rel = self.min_rel + np.random.random() * (self.max_rel - self.min_rel)

class Color(MultiTransform):
    def __init__(self, min_rel:float, max_rel:float):
        super().__init__()

        if min_rel < 0 or max_rel < 0 or min_rel > max_rel:
            raise Exception(f'min_rel and max_rel expected to be greater or equal 0. min_rel expected to be less or equal max_rel')

        self.__toTensor__ = ToTensor()
        self.__toPILImage__ = ToPILImage()

        self.min_rel = min_rel
        self.max_rel = max_rel

        self.__toCVImage__ = ToCVImage()

    def __call__(self, inputs):
        self.__get_size__(inputs)
        self.__reset__()
        is_tensor = isinstance(inputs[0], torch.Tensor)
        if not is_tensor:
            inputs = self.__toTensor__(inputs)

        is_color_image = inputs[0].shape[0] == 3

        results = []
        for input in self.__toCVImage__(inputs):
            if not is_color_image:
                input = cv.cvtColor(input, cv.COLOR_GRAY2BGR)
            hsv = cv.cvtColor(input, cv.COLOR_BGR2HSV)
            h, s, v = cv.split(hsv)

            h *= self.rel
            h[h > 360] = 360
            h[h < 0] = 0
            hsv = cv.merge((h, s, v))
            result = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)

            if not is_color_image:
                result = cv.cvtColor(result, cv.COLOR_BGR2GRAY)

            results.append(result)
        
        results = self.__toTensor__(results)

        if not is_tensor:
            results = self.__toPILImage__(results)
        return results
    
    def __reset__(self):
        self.rel = self.min_rel + np.random.random() * (self.max_rel - self.min_rel)

class GaussianNoise(MultiTransform):
    def __init__(self, min_noise_level = 0., max_noise_level:float = 0.005):
        super().__init__()

        self.__toTensor__ = ToTensor()
        self.__toPILImage__ = ToPILImage()

        self.min_noise_level = min_noise_level
        self.max_noise_level = max_noise_level

        self.__toCVImage__ = ToCVImage()

    def __call__(self, inputs):
        self.__get_size__(inputs)
        self.__reset__()
        is_tensor = isinstance(inputs[0], torch.Tensor)
        if not is_tensor:
            inputs = self.__toTensor__(inputs)

        results = []
        for input in self.__toCVImage__(inputs):
            noise = -self.__noise_level__ + 2 * np.random.random(input.shape) * self.__noise_level__
            result = input + noise

            results.append(result)

        results = self.__toTensor__(results)

        if not is_tensor:
            results = self.__toPILImage__(results)
        return results
    
    def __reset__(self):
        self.__noise_level__ = self.min_noise_level + np.random.random() * (self.max_noise_level - self.min_noise_level)

class Stack(MultiTransform):
    def __init__(self):
        super().__init__()

        self.__toTensor__ = ToTensor()
        self.__toPILImage__ = ToPILImage()

    def __call__(self, inputs):
        self.__get_size__(inputs)
        self.__reset__()
        is_tensor = isinstance(inputs[0], torch.Tensor)
        if not is_tensor:
            inputs = self.__toTensor__(inputs)

        results = torch.stack(inputs)
        
        return results
    
    def __reset__(self):
        pass

class BGR2GRAY(MultiTransform):
    def __init__(self):
        super().__init__()

        self.__toTensor__ = ToTensor()
        self.__toCVImage__ = ToCVImage()
        self.__toPILImage__ = ToPILImage()

    def __call__(self, inputs):
        self.__get_size__(inputs)
        self.__reset__()
        is_tensor = isinstance(inputs[0], torch.Tensor)
        if not is_tensor:
            inputs = self.__toTensor__(inputs)

        results = []
        for input in self.__toCVImage__(inputs):
            result = cv.cvtColor(input, cv.COLOR_BGR2GRAY)

            results.append(result)
        
        results = self.__toTensor__(results)
        
        if not is_tensor:
            results = self.__toPILImage__(results)
        return results
    
    def __reset__(self):
        pass

class RandomHorizontalFlip(MultiTransform):
    def __init__(self):
        super().__init__()

        self.__toTensor__ = ToTensor()
        self.__toCVImage__ = ToCVImage()
        self.__toPILImage__ = ToPILImage()

    def __call__(self, inputs):
        self.__get_size__(inputs)
        self.__reset__()
        is_tensor = isinstance(inputs[0], torch.Tensor)
        if not is_tensor:
            inputs = self.__toTensor__(inputs)

        results = []
        for input in self.__toCVImage__(inputs):
            if self.__should_flip__:
                result = cv.flip(input, 1)
            else:
                result = input

            results.append(result)
        
        results = self.__toTensor__(results)
        
        if not is_tensor:
            results = self.__toPILImage__(results)
        return results
    
    def __reset__(self):
        self.__should_flip__ = np.random.random() > 0.5

class RandomVerticalFlip(MultiTransform):
    def __init__(self):
        super().__init__()

        self.__toTensor__ = ToTensor()
        self.__toCVImage__ = ToCVImage()
        self.__toPILImage__ = ToPILImage()

    def __call__(self, inputs):
        self.__get_size__(inputs)
        self.__reset__()
        is_tensor = isinstance(inputs[0], torch.Tensor)
        if not is_tensor:
            inputs = self.__toTensor__(inputs)

        results = []
        for input in self.__toCVImage__(inputs):
            if self.__should_flip__:
                result = cv.flip(input, 0)
            else:
                result = input

            results.append(result)
        
        results = self.__toTensor__(results)
        
        if not is_tensor:
            results = self.__toPILImage__(results)
        return results
    
    def __reset__(self):
        self.__should_flip__ = np.random.random() > 0.5

if __name__ == '__main__':
    transforms = Compose([
        ToTensor(),
        #RandomCrop(max_scale=1.1),
        #Normalize(0, 1),
        #Rotate(max_angle=5, auto_scale=True),
        #Resize((500, 500)),
        #RandomCrop(max_scale=1.05),
        #Color(0.5, 1.5),
        #BGR2GRAY(),
        #Brightness(0.5, 1.5),
        #GaussianNoise(0.0, 0.005),
        RGB2BGR(),
        Scale(0.5),
        #BGR2RGB(),
        #Stack(),
        #RandomHorizontalFlip(),
        #BGR2GRAY(),
        ToCVImage(),
    ])

    #sequence_dir = f'/media/schulzr/ACA02F26A02EF70C/data/tuc-actionpredictiondataset/sequences/realsense/train'
    sequence_dir = '/Users/schulzr/Documents/Datasets/tuc-actionpredictiondataset/sequences/realsense/train/A000C000S000SEQ000'

    imgs = [
        Image.open(f'{sequence_dir}/C000F00000_color.jpg'),
        Image.open(f'{sequence_dir}/C000F00001_color.jpg'),
        Image.open(f'{sequence_dir}/C000F00002_color.jpg'),
        Image.open(f'{sequence_dir}/C000F00003_color.jpg'),
        Image.open(f'{sequence_dir}/C000F00004_color.jpg'),
        Image.open(f'{sequence_dir}/C000F00005_color.jpg'),
        Image.open(f'{sequence_dir}/C000F00006_color.jpg'),
    ]

    for i in range(10):
        results = transforms(imgs)
        for img, result in zip(imgs, results):
            cv.imshow('img', np.asarray(img))
            cv.imshow('result', result)
            print(result.shape)
            cv.waitKey()
    pass