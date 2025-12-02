import { createContext } from 'react';
import HTTPClient from '../api/httpClient';

const ClientContext = createContext<HTTPClient | null>(null);

const ClientProvider = ({ children }: { children: React.ReactNode }) => {
  const client = new HTTPClient();

  return (
    <ClientContext.Provider value={client}>{children}</ClientContext.Provider>
  );
};

export { ClientProvider, ClientContext };
