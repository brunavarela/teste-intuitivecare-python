<template>
  <div>
    <h1>Bem-vindo ao sistema de busca de Operadoras</h1>
    <SearchForm />
  </div>
</template>

<script>
import SearchForm from '../components/searchForm';

export default {
  components: {
    SearchForm,
  },
};
</script>

<style scoped>
h1 {
  text-align: center;
  margin-top: 20px;
}
</style>
