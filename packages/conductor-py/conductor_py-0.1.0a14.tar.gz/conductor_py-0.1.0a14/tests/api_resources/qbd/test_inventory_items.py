# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from conductor import Conductor, AsyncConductor
from tests.utils import assert_matches_type
from conductor._utils import parse_date
from conductor.types.qbd import InventoryItem
from conductor.pagination import SyncCursorPage, AsyncCursorPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestInventoryItems:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Conductor) -> None:
        inventory_item = client.qbd.inventory_items.create(
            name="Widget",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(InventoryItem, inventory_item, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Conductor) -> None:
        inventory_item = client.qbd.inventory_items.create(
            name="Widget",
            conductor_end_user_id="end_usr_1234567abcdefg",
            asset_account_id="80000009-1234567890",
            barcode={
                "allow_override": False,
                "assign_even_if_used": False,
                "bar_code_value": "1234567890",
            },
            class_id="80000001-1234567890",
            cogs_account_id="80000007-1234567890",
            external_id="12345678-abcd-1234-abcd-1234567890ab",
            income_account_id="80000005-1234567890",
            inventory_date=parse_date("2019-12-27"),
            is_active=True,
            manufacturer_part_number="MPN-123456",
            maximum_on_hand_quantity=200,
            parent_id="80000002-1234567890",
            preferred_vendor_id="80000008-1234567890",
            purchase_cost="15.75",
            purchase_description="Bulk purchase of steel bolts for inventory",
            purchase_tax_code_id="80000006-1234567890",
            quantity_on_hand=150,
            reorder_point=50,
            sales_description="High-quality steel bolts suitable for construction",
            sales_price="19.99",
            sales_tax_code_id="80000004-1234567890",
            total_value="1500.00",
            unit_of_measure_set_id="80000003-1234567890",
        )
        assert_matches_type(InventoryItem, inventory_item, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Conductor) -> None:
        response = client.qbd.inventory_items.with_raw_response.create(
            name="Widget",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inventory_item = response.parse()
        assert_matches_type(InventoryItem, inventory_item, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Conductor) -> None:
        with client.qbd.inventory_items.with_streaming_response.create(
            name="Widget",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inventory_item = response.parse()
            assert_matches_type(InventoryItem, inventory_item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Conductor) -> None:
        inventory_item = client.qbd.inventory_items.retrieve(
            id="80000001-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(InventoryItem, inventory_item, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Conductor) -> None:
        response = client.qbd.inventory_items.with_raw_response.retrieve(
            id="80000001-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inventory_item = response.parse()
        assert_matches_type(InventoryItem, inventory_item, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Conductor) -> None:
        with client.qbd.inventory_items.with_streaming_response.retrieve(
            id="80000001-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inventory_item = response.parse()
            assert_matches_type(InventoryItem, inventory_item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Conductor) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.qbd.inventory_items.with_raw_response.retrieve(
                id="",
                conductor_end_user_id="end_usr_1234567abcdefg",
            )

    @parametrize
    def test_method_list(self, client: Conductor) -> None:
        inventory_item = client.qbd.inventory_items.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(SyncCursorPage[InventoryItem], inventory_item, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Conductor) -> None:
        inventory_item = client.qbd.inventory_items.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
            class_ids="80000001-1234567890",
            cursor="12345678-abcd-abcd-example-1234567890ab",
            full_names="Furniture:Kitchen:Cabinet",
            ids="80000001-1234567890",
            limit=1,
            name_contains="nameContains",
            name_ends_with="nameEndsWith",
            name_from="nameFrom",
            name_starts_with="nameStartsWith",
            name_to="nameTo",
            status="active",
            updated_after="updatedAfter",
            updated_before="updatedBefore",
        )
        assert_matches_type(SyncCursorPage[InventoryItem], inventory_item, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Conductor) -> None:
        response = client.qbd.inventory_items.with_raw_response.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inventory_item = response.parse()
        assert_matches_type(SyncCursorPage[InventoryItem], inventory_item, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Conductor) -> None:
        with client.qbd.inventory_items.with_streaming_response.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inventory_item = response.parse()
            assert_matches_type(SyncCursorPage[InventoryItem], inventory_item, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncInventoryItems:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncConductor) -> None:
        inventory_item = await async_client.qbd.inventory_items.create(
            name="Widget",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(InventoryItem, inventory_item, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncConductor) -> None:
        inventory_item = await async_client.qbd.inventory_items.create(
            name="Widget",
            conductor_end_user_id="end_usr_1234567abcdefg",
            asset_account_id="80000009-1234567890",
            barcode={
                "allow_override": False,
                "assign_even_if_used": False,
                "bar_code_value": "1234567890",
            },
            class_id="80000001-1234567890",
            cogs_account_id="80000007-1234567890",
            external_id="12345678-abcd-1234-abcd-1234567890ab",
            income_account_id="80000005-1234567890",
            inventory_date=parse_date("2019-12-27"),
            is_active=True,
            manufacturer_part_number="MPN-123456",
            maximum_on_hand_quantity=200,
            parent_id="80000002-1234567890",
            preferred_vendor_id="80000008-1234567890",
            purchase_cost="15.75",
            purchase_description="Bulk purchase of steel bolts for inventory",
            purchase_tax_code_id="80000006-1234567890",
            quantity_on_hand=150,
            reorder_point=50,
            sales_description="High-quality steel bolts suitable for construction",
            sales_price="19.99",
            sales_tax_code_id="80000004-1234567890",
            total_value="1500.00",
            unit_of_measure_set_id="80000003-1234567890",
        )
        assert_matches_type(InventoryItem, inventory_item, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncConductor) -> None:
        response = await async_client.qbd.inventory_items.with_raw_response.create(
            name="Widget",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inventory_item = await response.parse()
        assert_matches_type(InventoryItem, inventory_item, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncConductor) -> None:
        async with async_client.qbd.inventory_items.with_streaming_response.create(
            name="Widget",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inventory_item = await response.parse()
            assert_matches_type(InventoryItem, inventory_item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncConductor) -> None:
        inventory_item = await async_client.qbd.inventory_items.retrieve(
            id="80000001-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(InventoryItem, inventory_item, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncConductor) -> None:
        response = await async_client.qbd.inventory_items.with_raw_response.retrieve(
            id="80000001-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inventory_item = await response.parse()
        assert_matches_type(InventoryItem, inventory_item, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncConductor) -> None:
        async with async_client.qbd.inventory_items.with_streaming_response.retrieve(
            id="80000001-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inventory_item = await response.parse()
            assert_matches_type(InventoryItem, inventory_item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncConductor) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.qbd.inventory_items.with_raw_response.retrieve(
                id="",
                conductor_end_user_id="end_usr_1234567abcdefg",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncConductor) -> None:
        inventory_item = await async_client.qbd.inventory_items.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(AsyncCursorPage[InventoryItem], inventory_item, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncConductor) -> None:
        inventory_item = await async_client.qbd.inventory_items.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
            class_ids="80000001-1234567890",
            cursor="12345678-abcd-abcd-example-1234567890ab",
            full_names="Furniture:Kitchen:Cabinet",
            ids="80000001-1234567890",
            limit=1,
            name_contains="nameContains",
            name_ends_with="nameEndsWith",
            name_from="nameFrom",
            name_starts_with="nameStartsWith",
            name_to="nameTo",
            status="active",
            updated_after="updatedAfter",
            updated_before="updatedBefore",
        )
        assert_matches_type(AsyncCursorPage[InventoryItem], inventory_item, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncConductor) -> None:
        response = await async_client.qbd.inventory_items.with_raw_response.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inventory_item = await response.parse()
        assert_matches_type(AsyncCursorPage[InventoryItem], inventory_item, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncConductor) -> None:
        async with async_client.qbd.inventory_items.with_streaming_response.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inventory_item = await response.parse()
            assert_matches_type(AsyncCursorPage[InventoryItem], inventory_item, path=["response"])

        assert cast(Any, response.is_closed) is True
