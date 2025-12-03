import clsx  from 'clsx';
import { twMerge } from 'tailwind-merge';

export function cn(...inputs) {
  return twMerge(clsx(inputs));
}

export const to12Hour = (t) => {
    const [h, m] = t.split(':');
    return `${h % 12 || 12}:${m} ${h >= 12 ? 'PM' : 'AM'}`;
};
