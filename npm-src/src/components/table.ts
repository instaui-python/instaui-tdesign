import type { SetupContext } from "vue";
import type { PaginationProps } from "tdesign-vue-next";
import { computed } from "vue";

export function usePagination(attrs: SetupContext["attrs"]) {
  return computed(() => {
    const { pagination } = attrs as { pagination: PaginationProps };

    if (typeof pagination === "boolean") {
      if (!pagination) {
        return undefined;
      }

      const { data = [] } = attrs as { data: any[] };

      const newPagination = {
        defaultCurrent: 1,
        defaultPageSize: 10,
        total: data.length,
      };

      return newPagination;
    }

    if (
      typeof pagination === "object" &&
      pagination !== null &&
      !("total" in pagination)
    ) {
      const { data = [] } = attrs as { data: any[] };
      return {
        defaultCurrent: 1,
        ...pagination,
        total: data.length,
      };
    }

    return pagination;
  });
}
