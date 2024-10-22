import torch
import torch.nn.functional as F
from typing import Union


def focal_loss(
    inputs: torch.Tensor,
    targets: torch.Tensor,
    gamma: float = 2.0,
    alpha: Union[float, int, list] = None,
    reduction: str = "mean",
    **kwargs
):
    """
    Focal Loss for unblanced classification problem.
    Args:
        inputs (torch.Tensor): model outputs
        targets (torch.Tensor): ground truth labels
        gamma (float): focal loss gamma
        alpha (Union[float, int, list]): alpha for focal loss
        reduction (str): reduction method
    Returns:
        torch.Tensor: focal loss
    """
    # Calculate the cross-entropy loss
    CE_loss = F.cross_entropy(inputs, targets, reduction="none")

    # Convert CE_loss to probabilities
    pt = torch.exp(-CE_loss)

    # Calculate the Focal Loss
    F_loss = (1 - pt) ** gamma * CE_loss

    if alpha is not None:
        if isinstance(alpha, (float, int)):
            alpha = torch.Tensor([1 - alpha, alpha]).to(inputs.device)
        elif isinstance(alpha, list):
            alpha = torch.Tensor(alpha).to(inputs.device)
        else:
            raise ValueError("alpha should be float, int or list")
        at = alpha.gather(0, targets)
        F_loss = at * F_loss

    if reduction == "mean":
        return F_loss.mean()
    elif reduction == "sum":
        return F_loss.sum()
    else:
        return F_loss


def binary_focal_loss(
    inputs: torch.Tensor,
    targets: torch.Tensor,
    gamma: float = 2.0,
    alpha: Union[float, int] = None,
    reduction: str = "mean",
    **kwargs
):
    """
    Focal Loss for binary classification problem.
    Args:
        inputs (torch.Tensor): model outputs
        targets (torch.Tensor): ground truth labels
        gamma (float): focal loss gamma
        alpha (Union[float, int]): alpha for focal loss
        reduction (str): reduction method
    Returns:
        torch.Tensor: binary focal loss
    """
    # Calculate the cross-entropy loss
    CE_loss = F.binary_cross_entropy_with_logits(inputs, targets, reduction="none")

    # Convert CE_loss to probabilities
    pt = torch.exp(-CE_loss)

    # Calculate the Focal Loss
    F_loss = (1 - pt) ** gamma * CE_loss

    if alpha is not None:
        if isinstance(alpha, (float, int)):
            alpha = torch.Tensor([1 - alpha, alpha]).to(inputs.device)
        else:
            raise ValueError("alpha should be float or int")
        at = alpha.gather(0, targets)
        F_loss = at * F_loss

    if reduction == "mean":
        return F_loss.mean()
    elif reduction == "sum":
        return F_loss.sum()
    else:
        return F_loss


def focal_loss_with_label_smoothing(
    inputs: torch.Tensor,
    targets: torch.Tensor,
    gamma: float = 2.0,
    alpha: Union[float, int, list] = None,
    reduction: str = "mean",
    smoothing: float = 0.1,
    num_classes: int = None,
    **kwargs
):
    """
    Focal Loss with label smoothing for unbalanced classification problem.
    Args:
        inputs (torch.Tensor): model outputs
        targets (torch.Tensor): ground truth labels
        gamma (float): focal loss gamma
        alpha (Union[float, int, list]): alpha for focal loss
        reduction (str): reduction method
        smoothing (float): label smoothing factor
        num_classes (int): number of classes
    Returns:
        torch.Tensor: focal loss with label smoothing
    """

    # Ensure num_classes is provided
    if num_classes is None:
        num_classes = inputs.shape[-1]

    # Calculate cross-entropy with label smoothing
    targets = targets.view(-1, 1)
    log_probs = F.log_softmax(inputs, dim=1)
    targets_one_hot = torch.zeros_like(log_probs).scatter(1, targets, 1)
    targets_smooth = (1.0 - smoothing) * targets_one_hot + smoothing / num_classes
    CE_loss = -torch.sum(targets_smooth * log_probs, dim=1)

    # Focal loss calculations
    pt = log_probs.gather(1, targets).view(-1).exp()

    F_loss = (1 - pt) ** gamma * CE_loss
    if alpha is not None:
        if isinstance(alpha, (float, int)):
            alpha = torch.Tensor([alpha, 1 - alpha]).to(inputs.device)
        elif isinstance(alpha, list):
            alpha = torch.Tensor(alpha).to(inputs.device)
        at = alpha.gather(0, targets.view(-1))
        F_loss = at * F_loss

    if reduction == "mean":
        return F_loss.mean()
    elif reduction == "sum":
        return F_loss.sum()
    else:
        return F_loss


def bce_with_logits(inputs: torch.Tensor, targets: torch.Tensor, **kwargs):
    """
    Binary cross entropy with logits
    Args:
        inputs (torch.Tensor): model outputs
        targets (torch.Tensor): ground truth labels
    Returns:
        torch.Tensor: binary cross entropy with logits
    """
    return F.binary_cross_entropy_with_logits(
        inputs, targets
    )  # , pos_weight=pos_weight.to(inputs.device))


def cross_entropy_from_probabilities(true_distributions, pred_distributions):
    """
    Calculates the cross entropy between two probability distributions that have already been applied with softmax.

    Parameters:
    - true_distributions: The actual distribution (target distribution). A PyTorch tensor.
    - pred_distributions: The predicted distribution. A PyTorch tensor.

    Returns:
    - The cross entropy value between the two distributions. (scalar)
    """
    # 두 분포 간의 cross entropy 계산
    cross_entropy = -torch.sum(
        true_distributions * torch.log(pred_distributions + 1e-9)
    )  # / true_distributions.size(0)
    return cross_entropy


def binary_cross_entropy_from_probabilities(true_distributions, pred_distributions):
    """
    두 확률 분포 사이의 이진 교차 엔트로피를 계산합니다. 이 확률 분포는 이미 softmax가 적용된 상태입니다.

    매개변수:
    - true_distributions: 실제 분포 (목표 분포). PyTorch 텐서.
    - pred_distributions: 예측 분포. PyTorch 텐서.

    반환값:
    - 두 분포 간의 이진 교차 엔트로피 값. (스칼라)
    """
    # 정밀도 문제를 피하기 위해 float32로 변환
    true_distributions = true_distributions.to(torch.float32)
    pred_distributions = pred_distributions.to(torch.float32)

    # 로그의 입력값이 0이 되는 것을 방지하기 위해 작은 epsilon 추가
    epsilon = 1e-4
    pred_distributions = torch.clamp(pred_distributions, epsilon, 1.0 - epsilon)

    # 이진 교차 엔트로피 계산
    binary_cross_entropy = -torch.sum(
        true_distributions * torch.log(pred_distributions)
        + (1 - true_distributions) * torch.log(1 - pred_distributions)
    )

    return binary_cross_entropy


LOSSES = {
    "cross_entropy": F.cross_entropy,
    "focal_loss": focal_loss,
    "focal_loss_with_label_smoothing": focal_loss_with_label_smoothing,
    "binary_cross_entropy": bce_with_logits,
    "binary_focal_loss": binary_focal_loss,
}
