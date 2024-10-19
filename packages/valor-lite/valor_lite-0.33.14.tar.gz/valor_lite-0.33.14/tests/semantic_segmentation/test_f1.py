from valor_lite.semantic_segmentation import (
    DataLoader,
    Metric,
    MetricType,
    Segmentation,
)


def test_f1_basic_segmentations(basic_segmentations: list[Segmentation]):
    loader = DataLoader()
    loader.add_data(basic_segmentations)
    evaluator = loader.finalize()

    metrics = evaluator.evaluate()

    actual_metrics = [m.to_dict() for m in metrics[MetricType.F1]]
    expected_metrics = [
        {
            "type": "F1",
            "value": 2 / 3,
            "parameters": {"label": "v1"},
        },
        {
            "type": "F1",
            "value": 2 / 3,
            "parameters": {"label": "v2"},
        },
    ]
    for m in actual_metrics:
        assert m in expected_metrics
    for m in expected_metrics:
        assert m in actual_metrics


def test_f1_segmentations_from_boxes(
    segmentations_from_boxes: list[Segmentation],
):
    loader = DataLoader()
    loader.add_data(segmentations_from_boxes)
    evaluator = loader.finalize()

    metrics = evaluator.evaluate()

    actual_metrics = [m.to_dict() for m in metrics[MetricType.F1]]
    expected_metrics = [
        {
            "type": "F1",
            "value": 0.5,  # 50% overlap
            "parameters": {"label": "v1"},
        },
        {
            "type": "F1",
            "value": 1 / 10000,  # overlaps 1 pixel out of 20,000
            "parameters": {"label": "v2"},
        },
    ]
    for m in actual_metrics:
        assert m in expected_metrics
    for m in expected_metrics:
        assert m in actual_metrics


def test_f1_large_random_segmentations(
    large_random_segmentations: list[Segmentation],
):
    loader = DataLoader()
    loader.add_data(large_random_segmentations)
    evaluator = loader.finalize()

    metrics = evaluator.evaluate()

    for m in metrics[MetricType.F1]:
        assert isinstance(m, Metric)
        match m.parameters["label"]:
            case "v1":
                assert round(m.value, 1) == 0.9  # type: ignore - testing
            case "v2":
                assert round(m.value, 2) == 0.09  # type: ignore - testing
            case "v3":
                assert round(m.value, 2) == 0.01  # type: ignore - testing
            case "v4":
                assert round(m.value, 1) == 0.4  # type: ignore - testing
            case "v5":
                assert round(m.value, 1) == 0.4  # type: ignore - testing
            case "v6":
                assert round(m.value, 1) == 0.1  # type: ignore - testing
            case "v7":
                assert round(m.value, 1) == 0.3  # type: ignore - testing
            case "v8":
                assert round(m.value, 1) == 0.3  # type: ignore - testing
            case "v9":
                assert round(m.value, 1) == 0.3  # type: ignore - testing
            case _:
                assert False
