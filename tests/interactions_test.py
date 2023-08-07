from pages.interactions_page import SortablePage, SelectablePage, ResizablePage, DroppablePage
from locators.interactions_page_locators import SortablePageLocators, SelectablePageLocators, ResizablePageLocators, \
    DroppablePageLocators
import pytest

class TestInteractions:

    class TestSortablePage:
        locators = SortablePageLocators

        test_data = {
            "list": {
                "tab": locators.TAB_LIST,
                "items": locators.LIST_ITEMS,
                "expected_list": ['Two', 'Three', 'Four', 'Five', 'Six', 'One']
            },
            "grid": {
                "tab": locators.TAB_GRID,
                "items": locators.GRID_ITEMS,
                "expected_list": ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'One']
            }
        }

        @pytest.mark.parametrize("data", test_data.values(), ids=test_data.keys())
        def test_sortable_random(self, driver, data):
            sortable_page = SortablePage(driver, 'https://demoqa.com/sortable')
            sortable_page.open()
            order_before, order_after = sortable_page.change_random_item_order(data["tab"], data["items"])
            assert order_before != order_after, \
                f'Order before: {order_before} and order after: {order_after} are equal, but difference was expected'

        @pytest.mark.parametrize("data", test_data.values(), ids=test_data.keys())
        def test_sortable_one_to_end(self, driver, data):
            sortable_page = SortablePage(driver, 'https://demoqa.com/sortable')
            sortable_page.open()
            order_after = sortable_page.move_one_to_end(data["tab"], data["items"])
            assert order_after == data["expected_list"], \
                f"Unexpected order of items {order_after}"

    class TestSelectablePage:
        locators = SelectablePageLocators()

        test_data = {
            "list": {
                "tab": locators.TAB_LIST,
                "items": locators.LIST_ITEMS,
                "selected": locators.ACTIVE_LIST_ITEMS
            },
            "grid": {
                "tab": locators.TAB_GRID,
                "items": locators.GRID_ITEMS,
                "selected": locators.ACTIVE_LIST_GRID
            }
        }

        @pytest.mark.parametrize("data", test_data.values(), ids=test_data.keys())
        def test_selectable_random(self,driver, data):
            selectable_page = SelectablePage(driver, 'https://demoqa.com/selectable')
            selectable_page.open()
            items_for_select, selected_items = selectable_page.select_random_items(data["tab"], data["items"],
                                                                                   data["selected"])
            """Создаём неупорядоченные множества на основе списков"""
            items = set(items_for_select)
            selected = set(selected_items)
            """Сравниваем, 2 множества равны, если содержат одинаковые элементы"""
            assert items == selected, f"Clicked items: {items} and selected items {selected} are different"

    class TestResizablePage:

        def test_resizable_box(self, driver):
            resizable_page = ResizablePage(driver, 'https://demoqa.com/resizable')
            resizable_page.open()
            default_size, min_size,  max_size = resizable_page.change_resizable_box_size()
            assert default_size == {'height': 200, 'width': 200}, f"Size {default_size} different from expected default"
            assert min_size == {'height': 150, 'width': 150}, f"Size {min_size} different from expected min size"
            assert max_size == {'height': 300, 'width': 500}, f"Size {max_size} different from expected max size"

        def test_resizable(self, driver):
            resizable_page = ResizablePage(driver, 'https://demoqa.com/resizable')
            resizable_page.open()
            default_size, min_size,  max_size = resizable_page.change_resizable_size()
            assert default_size == {'height': 200, 'width': 200}, f"Size {default_size} different from expected default"
            assert min_size == {'height': 20, 'width': 20}, f"Size {min_size} different from expected min size"
            assert max_size == {'height': 520, 'width': 520}, f"Size {max_size} different from expected max size"

    class TestDroppablePage:
        class TestSimple:
            def test_drag_simple(self, driver):
                simple_page = DroppablePage(driver, 'https://demoqa.com/droppable')
                simple_page.open()
                text_before, text_after = simple_page.drag_simple()
                assert text_before == "Drop here", "Incorrect text before drag action"
                assert text_after == "Dropped!", "Incorrect text after drag action"

        class TestAccept:
            locators = DroppablePageLocators()
            data = {
                "acceptable": {
                    "locator":locators.ACCEPTABLE,
                    "expected_text": "Dropped!"
                },
                "not_acceptable": {
                    "locator": locators.NOT_ACCEPTABLE,
                    "expected_text": "Drop here"
                }
            }
            @pytest.mark.parametrize("data", data.values(), ids=data.keys())
            def test_drag_accept(self, driver, data):
                accept_page = DroppablePage(driver, 'https://demoqa.com/droppable')
                accept_page.open()
                text_before, text_after = accept_page.drag_accept(data["locator"])
                assert text_before == "Drop here", "Incorrect text before drag action"
                assert text_after == data["expected_text"], "Incorrect text after drag action"

        class TestPrevent:
            locators = DroppablePageLocators()
            data = {
                "outer_not_greedy": {
                    "drop": locators.PREVENT_NOT_GREEDY_OUTER,
                    "neighbor": locators.PREVENT_NOT_GREEDY_INNER,
                    "expected_before": ['Outer droppable', 'Inner droppable (not greedy)'],
                    "expected_after": ['Dropped!', 'Inner droppable (not greedy)']
                },
                "outer_greedy": {
                    "drop": locators.PREVENT_GREEDY_OUTER,
                    "neighbor": locators.PREVENT_GREEDY_INNER,
                    "expected_before": ['Outer droppable', 'Inner droppable (greedy)'],
                    "expected_after": ['Dropped!', 'Inner droppable (greedy)']
                },
                "inner_not_greedy": {
                    "drop": locators.PREVENT_NOT_GREEDY_INNER,
                    "neighbor": locators.PREVENT_NOT_GREEDY_OUTER,
                    "expected_before": ['Inner droppable (not greedy)', 'Outer droppable'],
                    "expected_after": ['Dropped!', 'Dropped!']
                },
                "inner_greedy": {
                    "drop": locators.PREVENT_GREEDY_INNER,
                    "neighbor": locators.PREVENT_GREEDY_OUTER,
                    "expected_before": ['Inner droppable (greedy)', 'Outer droppable'],
                    "expected_after": ['Dropped!', 'Outer droppable']
                }
            }

            @pytest.mark.parametrize("data", data.values(), ids=data.keys())
            def test_prevent_drag_outers(self, driver, data):
                prevent_page = DroppablePage(driver, 'https://demoqa.com/droppable')
                prevent_page.open()
                text_before, text_after = prevent_page.drag_prevent(data["drop"], data["neighbor"])
                assert text_before == data["expected_before"], "Incorrect text before dragging"
                assert text_after == data["expected_after"], "Incorrect text after dragging"

        class TestRevert:
            def test_revertable(self, driver):
                revert_page = DroppablePage(driver, 'https://demoqa.com/droppable')
                revert_page.open()
                text_before, location_before, text_after, location_after = revert_page.drag_revert()
                assert text_before == "Drop here", "Incorrect text before dragging"
                assert location_before != location_after and location_after == \
                       "position: relative; left: 0px; top: 0px;"
                assert text_after == "Dropped!"

            def test_not_revertable(self, driver):
                revert_page = DroppablePage(driver, 'https://demoqa.com/droppable')
                revert_page.open()
                text_before, location_before, text_after, location_after, location_leave = revert_page.drag_not_revert()
                assert text_before == "Drop here", "Incorrect text before dragging"
                assert location_before != location_after and location_after == \
                       "position: relative; left: 314px; top: -17px;"
                #дополнительно проверяем что элемент можно вытянуть из дива
                assert location_leave != location_after, "Div didn't change location after dragging out of drop div"
