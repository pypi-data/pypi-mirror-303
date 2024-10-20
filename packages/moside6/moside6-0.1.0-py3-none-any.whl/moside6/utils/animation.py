from typing import Union

from PySide6.QtCore import QPropertyAnimation, QEasingCurve, QRect


def create_animation(
        instance,
        property_name: bytes,
        start_value: Union[int, float, QRect],
        end_value: Union[int, float],
        duration=300,
        easing_curve=QEasingCurve.OutQuart,
        loop_count=1):
    """
    创建属性动画
    Args:
        instance: 要操作的实例
        property_name: 要操作的属性
        start_value: 动画开始值
        end_value: 动画结束值
        duration: 动画持续时间
        easing_curve: 动画曲线
        loop_count: 动画循环次数

    Returns: 动画对象
    """
    animation = QPropertyAnimation(instance, property_name)
    animation.setDuration(duration)
    animation.setStartValue(start_value)
    animation.setEndValue(end_value)
    animation.setEasingCurve(easing_curve)
    animation.setLoopCount(loop_count)
    return animation
