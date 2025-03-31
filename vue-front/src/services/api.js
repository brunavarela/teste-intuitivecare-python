import axios from "axios";

const API_URL = "http://localhost:5000";

export const buscarOperadoras = async (termo) => {
  try {
    const response = await axios.get(`${API_URL}/buscar_operadoras?termo=${termo}`);
    return response.data;
  } catch (error) {
    console.error("Erro ao buscar operadoras:", error);
    throw new Error("Erro ao buscar operadoras. Tente novamente.");
  }
};
