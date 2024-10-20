from enum import Enum


class ModeEnum(Enum):
    """
    方法を表すEnumクラス
    """

    INCOME = 1
    PAYMENT = 2
    TRANSFER = 3

    @classmethod
    def from_str(cls, mode_str: str):
        """
        文字列からEnumへの変換を行うクラスメソッド
        """
        mapping = {
            "payment": cls.PAYMENT,
            "income": cls.INCOME,
            "transfer": cls.TRANSFER,
        }
        return mapping.get(mode_str, None)


def get_mode_id(mode: str) -> int:
    """
    方法の文字列をEnumの値に変換する関数
    """
    mode_enum = ModeEnum.from_str(mode)
    return mode_enum.value if mode_enum else None


def get_unique_places(data) -> list:
    """
    データからユニークなお店のリストを取得する
    """
    unique_places = set()
    unique_places_result = []

    for entry in data:
        place_name = entry.get("place")

        # お店名が存在し、まだユニークなお店のセットに含まれていない場合
        if place_name and place_name not in unique_places:
            unique_places_result.append(
                {key: entry[key] for key in ["place", "place_uid"] if key in entry}
            )
            unique_places.add(place_name)
    return unique_places_result
