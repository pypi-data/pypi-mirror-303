import torch
import torch.nn.functional as F
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sn
import pandas as pd
import cv2 as cv

def confusion_matrix(Y, T):
    num_classes = T.shape[1]
    classes_Y = torch.argmax(Y, dim=1)
    classes_T = torch.argmax(T, dim=1)

    cm = torch.zeros((num_classes, num_classes), dtype=torch.int64)

    for cy, ct in zip(classes_Y, classes_T):
        cm[ct, cy] += 1

    return cm

def confusion(Y, T):
    """ Returns the confusion matrix for the values in the `prediction` and `truth`
        tensors, i.e. the amount of positions where the values of `prediction`
        and `truth` are
        - 1 and 1 (True Positive)
        - 1 and 0 (False Positive)
        - 0 and 0 (True Negative)
        - 0 and 1 (False Negative)
        """
    confusion_vector = Y / T
    # Element-wise division of the 2 tensors returns a new tensor which holds a
    # unique value for each case:
    #   1     where prediction and truth are 1 (True Positive)
    #   inf   where prediction is 1 and truth is 0 (False Positive)
    #   nan   where prediction and truth are 0 (True Negative)
    #   0     where prediction is 0 and truth is 1 (False Negative)
    true_positives = torch.sum(confusion_vector == 1).item()
    false_positives = torch.sum(confusion_vector == float('inf')).item()
    true_negatives = torch.sum(torch.isnan(confusion_vector)).item()
    false_negatives = torch.sum(confusion_vector == 0).item()
    return true_positives, false_positives, true_negatives, false_negatives

def TP(Y, T):
    assert torch.all(Y <= 1) and torch.all(Y >= 0), 'Expected 0 <= Y <= 1'
    
    Y_pos = Y >= 0.5
    T_pos = T >= 0.5

    mask = torch.bitwise_and(Y_pos, T_pos)
    tp = mask.sum().item()
    return tp

def TN(Y, T):
    assert torch.all(Y <= 1) and torch.all(Y >= 0), 'Expected 0 <= Y <= 1'
    
    Y_neg = Y < 0.5
    T_neg = T < 0.5

    mask = torch.bitwise_and(Y_neg, T_neg)
    tn = mask.sum().item()
    return tn

def FP(Y, T):
    assert torch.all(Y <= 1) and torch.all(Y >= 0), 'Expected 0 <= Y <= 1'
    
    Y_pos = Y >= 0.5
    T_neg = T < 0.5

    mask = torch.bitwise_and(Y_pos, T_neg)
    fp = mask.sum().item()
    return fp

def FN(Y, T):
    assert torch.all(Y <= 1) and torch.all(Y >= 0), 'Expected 0 <= Y <= 1'
    
    Y_neg = Y < 0.5
    T_pos = T >= 0.5

    mask = torch.bitwise_and(Y_neg, T_pos)
    fn = mask.sum().item()
    return fn

def FPR(Y, T):
    fp = FP(Y, T)
    tn = TN(Y, T)
    if fp + tn == 0:
        return np.nan
    fpr = fp / (fp + tn)
    return fpr

def TPR(Y, T):
    tp = TP(Y, T)
    fn = FN(Y, T)
    if tp + fn == 0:
        return np.nan
    tpr = tp / (tp + fn)
    return tpr

def F1_Score(Y, T):
    tp = TP(Y, T)
    fp = FP(Y, T)
    fn = FN(Y, T)
    if tp + fp + fn == 0:
        return np.nan
    f1score = 2 * tp / (2 * tp + fp + fn)
    return f1score

def top_k_accuracy(Y:torch.Tensor, T:torch.Tensor, k:int):
    top_k_prediction = torch.argsort(Y, dim=1, descending=True)[:, :k]
    top_1_target = torch.argmax(T, dim=1)

    tp = 0
    for y, t in zip(top_k_prediction, top_1_target):
        if t in y:
            tp += 1
        pass

    acc = tp / T[:, 0].numel()
    return acc

def top_1_accuracy(Y:torch.Tensor, T:torch.Tensor):
    return top_k_accuracy(Y, T, 1)

def top_3_accuracy(Y:torch.Tensor, T:torch.Tensor):
    return top_k_accuracy(Y, T, 3)

def plot_confusion_matrix(
        confusion_matrix:torch.Tensor,
        labels = None,
        cmap:str = 'Blues',
        xlabel:str = 'Predicted label',
        ylabel:str = 'True label',
        title:str = 'Confusion Matrix',
        plt_show:bool = False,
        save_file_name:str = None) -> np.array:
    if labels is None:
        labels = [f'Class {i+1}' for i in range(confusion_matrix.shape[0])]

    df_cm = pd.DataFrame(confusion_matrix, index = [i for i in labels],
                  columns = [i for i in labels])
    fig = plt.figure(figsize = (10,7))

    sn.heatmap(df_cm, annot=True, cmap=cmap, fmt='g')
    plt.xticks(rotation=45, ha="right")
    plt.yticks(rotation=0, ha="right")
    if title is not None:
        plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    if plt_show:
        plt.show()

    fig.canvas.draw()

    s, (width, height) = fig.canvas.print_to_buffer()

    # Option 2a: Convert to a NumPy array.
    img = np.fromstring(s, np.uint8).reshape((height, width, 4))
    img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

    if save_file_name is not None:
        cv.imwrite(save_file_name, img)

    plt.close()

    return img

if __name__ == '__main__':
    Y = torch.tensor([
        [0.1, 0.1, 0.8],
        [0.95, 0.03, 0.02],
        [0.05, 0.9, 0.05]
    ])
    T = torch.tensor([
        [0, 0, 1],
        [1, 0, 0],
        [0, 1, 0]
    ])

    tp = TP(Y, T)
    tn = TN(Y, T)
    fp = FP(Y, T)
    fn = FN(Y, T)

    f1 = F1_Score(Y, T)

    epsilon = 0.2
    num_elements = 10000
    num_classes = 7

    T = []
    for i in range(num_elements):
        true_class = torch.randint(0, num_classes, (1,))
        t = F.one_hot(true_class, num_classes=num_classes)
        T.append(t)
    T = torch.cat(T)

    dist = torch.normal(T.float(), 1.5)
    Y = torch.argmax(dist, dim=1)
    Y = F.one_hot(Y, num_classes=num_classes)

    conf_m = confusion_matrix(Y, T)
    print(conf_m)

    labels = []
    for a in range(num_classes):
        a_str = str(a)
        while len(a_str) < 3:
            a_str = '0' + a_str
        a_str = 'A' + a_str
        labels.append(a_str)

    img = plot_confusion_matrix(conf_m, labels=labels, plt_show=True)