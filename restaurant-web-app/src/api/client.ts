import { useContext } from 'react';
import { ClientContext } from '../context/HTTPClientProvider';

export const useClient = () => {
  const client = useContext(ClientContext);
  if (!client)
    throw new Error('useClient must be used within a ClientProvider');
  return client;
};