import { type App } from "vue";
import TDesign from "tdesign-vue-next";
import "./style.css";
import Table from "@/components/Table.vue";

function install(app: App) {
  app.use(TDesign);
  app.component("t-table", Table);
}

export { install };
