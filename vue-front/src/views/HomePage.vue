<template>
  <div class="main-container">
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
  .main-container {
    background: linear-gradient(to right, #021D18 20%, #05060A 80%); 
    display: flex;
    height: 100vh;
    flex-direction: column;
    align-items: center;
    text-align: center;
    padding: 40px;
    color: white;
  }

  h1 {
    text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
    font-size: 24px;
  }

  @media screen and (min-width: 1400px) {
    .main-container {
      padding-top: 100px;
    }
  }

  @media screen and (min-width: 768px) {
    h1 {
      max-width: 400px;
      font-size: 28px;
    }
  }
</style>
