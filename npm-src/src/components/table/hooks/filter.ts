import type { TableProps } from "tdesign-vue-next";
import { ref, type SetupContext } from "vue";
import { orderBy as _orderBy, uniqBy as _uniqBy } from "lodash-es";
import type {
  TTableData,
  TTableRowsHandler,
  TTableColumns,
  TTableColumnsWithInfer,
  TTableColumnHandler,
} from "../types";

export function useTableFilter(options: {
  tableData: TTableData;
  registerRowsHandler: (handler: TTableRowsHandler) => void;
  attrs: SetupContext["attrs"];
  columns: TTableColumnsWithInfer;
  registerColumnsHandler: (handler: TTableColumnHandler) => void;
  tdesignGlobalConfig: Record<string, any>;
}) {
  const { tableData, registerColumnsHandler, registerRowsHandler, columns } =
    options;

  registerColumnsHandler(
    (columns) =>
      columns.map((column) =>
        normalizeTableFilterRecord(
          column,
          tableData,
          options.tdesignGlobalConfig
        )
      ) as TTableColumns
  );

  const filterValue = ref<TableProps["filterValue"]>();

  const colKey2Info = new Map(columns.value.map((col) => [col.colKey, col]));

  registerRowsHandler((rows) => {
    if (!filterValue.value) {
      return rows;
    }

    const filterInfos = Object.keys(filterValue.value).map((key) => {
      const value = (filterValue.value as any)[key] as any;
      const type = colKey2Info.get(key)!.filter!.type!;

      return {
        key,
        value,
        type,
      };
    });

    return rows.filter((row) => {
      return filterInfos.every((info) => {
        if (info.type === "multiple") {
          const filterValues = info.value as string[];
          if (filterValues.length === 0) return true;
          return filterValues.includes(row[info.key]);
        }

        if (info.type === "single") {
          const filterValue = info.value as any;
          if (!filterValue) return true;
          return row[info.key] === filterValue;
        }

        if (info.type === "input") {
          const filterValue = info.value as string;
          if (!filterValue) return true;
          return row[info.key].toString().includes(filterValue);
        }

        throw new Error("not support filter type");
      });
    });
  });

  const onFilterChange: TableProps["onFilterChange"] = (filters, ctx) => {
    if (!ctx.col) {
      filterValue.value = undefined;
      return;
    }
    filterValue.value = {
      ...filters,
    };
  };

  function resetFilters() {
    filterValue.value = undefined;
  }

  function filterResultText(): string | null {
    if (!filterValue.value) return null;

    return Object.keys(filterValue.value)
      .map((key) => {
        const label = colKey2Info.get(key)!.label;
        const values = filterValue.value![key];
        if (values.length === 0) {
          return "";
        }
        return `${label}: ${JSON.stringify(values)}`;
      })
      .join("; ");
  }

  return {
    onFilterChange,
    filterValue,
    resetFilters,
    filterResultText,
  };
}

function normalizeTableFilterRecord(
  column: Record<string, any>,
  tableData: TTableData,
  tdesignGlobalConfig: Record<string, any>
) {
  const hasFilter = "filter" in column;

  if (!hasFilter) {
    return column;
  }

  if (!("type" in column.filter)) throw new Error("filter type is required");

  const { colKey } = column;
  const { type } = column.filter as { type: "multiple" | "single" | "input" };

  if (type === "multiple") {
    const list = _uniqBy(tableData.value, colKey).map((item) => {
      return {
        label: item[colKey],
        value: item[colKey],
      };
    });

    const newFilter = {
      resetValue: [],
      list: [
        { label: tdesignGlobalConfig.selectAllText, checkAll: true },
        ...list,
      ],
      ...column.filter,
    };

    return {
      ...column,
      filter: newFilter,
    };
  }

  if (type === "single") {
    const list = _uniqBy(tableData.value, colKey).map((item) => {
      return {
        label: item[colKey],
        value: item[colKey],
      };
    });

    const newFilter = {
      resetValue: null,
      list,
      showConfirmAndReset: true,
      ...column.filter,
    };

    return {
      ...column,
      filter: newFilter,
    };
  }

  if (type === "input") {
    const newFilter = {
      resetValue: "",
      confirmEvents: ["onEnter"],
      showConfirmAndReset: true,
      ...column.filter,
      props: {
        ...column.filter?.props,
      },
    };

    return {
      ...column,
      filter: newFilter,
    };
  }

  throw new Error("not support filter type");
}
