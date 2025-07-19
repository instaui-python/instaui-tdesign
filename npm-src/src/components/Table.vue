<script setup lang="ts">
import { Table } from "tdesign-vue-next";
import { useAttrs, useSlots } from "vue";
import { usePagination } from "./table";

defineOptions({ inheritAttrs: false });

const attrs = useAttrs();
const pagination = usePagination(attrs);

const slots = useSlots();
</script>

<template>
  <Table v-bind="attrs" :pagination="pagination">
    <template v-for="(_, name) in slots" v-slot:[name]="slotProps" :key="name">
      <slot :name="name" v-bind="slotProps" />
    </template>
  </Table>
</template>

<style scoped></style>
